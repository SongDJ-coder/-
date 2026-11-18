# coding: utf-8
"""
CONTEXUS 공부 기록 더미 데이터 — '꾸민 공부 기록 판별기' 연습용

기록 한 묶음 = 한 사용자가 한 문서를 공부한 기록 전체.
묶음 하나를 숫자 8개(입력)로 줄이고, 정답은 0 = 진짜 공부 / 1 = 꾸민 기록.

🔴 전부 가짜 데이터다. 실제 사용자 기록은 하나도 쓰지 않았다.
🔴 아래 분포(평균 · 퍼짐)는 '그럴듯하다'고 추정해서 정한 값이다. 실제 측정값이 아니다.
   그래서 이 데이터로 배운 모델은 '여기 적힌 규칙'을 다시 찾아낼 뿐이다.

사용법 (책의 load_mnist 와 같은 모양):
    from make_dummy import load_dummy, FEATURES
    (x_train, t_train), (x_test, t_test) = load_dummy(one_hot_label=True)
"""
import numpy as np

# 입력 8칸의 이름 · 뜻 · 단위
FEATURES = [
    ('paste_ratio',   '붙여넣기로 들어온 질문 비율',           '0~1'),
    ('dwell_sec',     '쪽마다 머문 평균 시간',                 '초'),
    ('followup_ratio','앞 답을 받아 이어 물은 꼬리 질문 비율', '0~1'),
    ('page_match',    '질문이 그 쪽 내용과 맞는 정도',          '0~1'),
    ('study_days',    '이 문서를 공부한 날 수',                '일'),
    ('interval_cv',   '질문 사이 간격이 들쭉날쭉한 정도',       '변동계수'),
    ('typing_speed',  '질문을 입력한 속도',                    '글자/초'),
    ('revisit_ratio', '앞에서 본 쪽으로 돌아간 비율',           '0~1'),
]
FEATURE_NAMES = [f[0] for f in FEATURES]
LABEL_NAMES = ['진짜', '꾸밈']


def _honest(rng, n):
    """진짜로 공부한 기록: 직접 치고, 오래 읽고, 꼬리 질문이 많고, 여러 날에 걸쳐 들쭉날쭉."""
    x = np.column_stack([
        rng.beta(1.5, 12, n),                    # 붙여넣기 거의 없음
        rng.lognormal(np.log(120), 0.5, n),      # 쪽마다 2분 안팎
        rng.beta(4, 4, n),                       # 꼬리 질문 절반쯤
        rng.beta(8, 2, n),                       # 쪽 내용과 잘 맞음
        1 + rng.poisson(6, n),                   # 일주일 안팎
        rng.normal(1.0, 0.3, n),                 # 사람이라 간격이 불규칙
        rng.normal(4, 1.2, n),                   # 사람 손 타자 속도
        rng.beta(3, 6, n),                       # 앞 쪽을 자주 다시 봄
    ])
    # 진짜인데 붙여넣기가 많은 사람 (PDF 문장을 복사해 묻는 습관) — 5%
    k = rng.random(n) < 0.05
    x[k, 0] = rng.beta(6, 3, k.sum())
    x[k, 6] = rng.normal(9, 3, k.sum())
    return x


def _fake_paste(rng, n):
    """꾸밈 A — 다른 AI가 만든 그럴듯한 질문을 붙여 넣음."""
    return np.column_stack([
        rng.beta(8, 2, n),
        rng.lognormal(np.log(40), 0.6, n),       # 읽지 않고 넘김
        rng.beta(1.5, 6, n),                     # 이어 묻지 않음
        rng.beta(4, 3, n),                       # 일반적인 질문이라 쪽과 덜 맞음
        1 + rng.poisson(2, n),                   # 하루 이틀에 몰아서
        rng.normal(0.5, 0.25, n),
        rng.normal(15, 5, n),                    # 붙여 넣으니 '속도'가 비정상적으로 빠름
        rng.beta(1.5, 8, n),
    ])


def _fake_idle(rng, n):
    """꾸밈 B — 페이지만 띄워 두고 날짜와 시간을 채움."""
    return np.column_stack([
        rng.beta(2, 6, n),
        rng.lognormal(np.log(600), 0.4, n),      # 자리를 비워 시간만 김
        rng.beta(1.2, 8, n),
        rng.beta(3, 3, n),
        1 + rng.poisson(10, n),                  # 날 수는 많음
        rng.normal(0.3, 0.15, n),                # 정해진 간격으로 기계적으로
        rng.normal(5, 1.5, n),
        rng.beta(1, 12, n),
    ])


def make_records(n, fake_rate=0.2, seed=0):
    """기록 n개를 만든다. 반환: x (n, 8), t (n,) 정답 숫자 0/1"""
    rng = np.random.default_rng(seed)
    n_fake = int(n * fake_rate)
    n_a = int(n_fake * 0.6)
    n_b = n_fake - n_a
    x = np.vstack([_honest(rng, n - n_fake), _fake_paste(rng, n_a), _fake_idle(rng, n_b)])
    t = np.concatenate([np.zeros(n - n_fake, int), np.ones(n_fake, int)])

    # 진짜처럼 잘 꾸민 기록 — 꾸밈의 10%를 진짜 쪽으로 반쯤 끌어당김 (완벽히 맞히지 못하게)
    fake_idx = np.where(t == 1)[0]
    clever = rng.choice(fake_idx, int(len(fake_idx) * 0.1), replace=False)
    x[clever] = 0.5 * x[clever] + 0.5 * _honest(rng, len(clever))

    # 값의 범위 정리
    for j in (0, 2, 3, 7):
        x[:, j] = np.clip(x[:, j], 0, 1)
    x[:, 1] = np.clip(x[:, 1], 5, 1800)
    x[:, 5] = np.clip(x[:, 5], 0.05, None)
    x[:, 6] = np.clip(x[:, 6], 0.5, None)

    order = rng.permutation(n)                   # 진짜 · 꾸밈이 섞이게
    return x[order], t[order]


def _one_hot(t, k=2):
    T = np.zeros((t.size, k))
    T[np.arange(t.size), t] = 1
    return T


def load_dummy(n_train=3000, n_test=1000, one_hot_label=True, seed=0):
    """(x_train, t_train), (x_test, t_test) — 정규화는 하지 않은 원래 값"""
    x_train, t_train = make_records(n_train, seed=seed)
    x_test, t_test = make_records(n_test, seed=seed + 1)
    if one_hot_label:
        t_train, t_test = _one_hot(t_train), _one_hot(t_test)
    return (x_train, t_train), (x_test, t_test)


if __name__ == '__main__':
    (x, t), _ = load_dummy(one_hot_label=False)
    print('x', x.shape, '| 꾸밈 비율', t.mean())
    for j, (name, desc, unit) in enumerate(FEATURES):
        print(f'{name:15s} 진짜 {x[t == 0, j].mean():8.2f} | 꾸밈 {x[t == 1, j].mean():8.2f}  ({unit}) {desc}')
