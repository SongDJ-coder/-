# 밑바닥부터 시작하는 딥러닝 — 실습 폴더

## 폴더 구조
| 폴더 | 내용 |
|---|---|
| `ch01_python` | 1장 파이썬·NumPy·matplotlib 기초 |
| `ch02_perceptron` | 2장 퍼셉트론 |
| `ch03_neural_network` | 3장 신경망 |
| `ch04_learning` | 4장 신경망 학습 |
| `ch05_backprop` | 5장 오차역전파법 |
| `ch06_techniques` | 6장 학습 관련 기술 |
| `ch07_cnn` | 7장 CNN |
| `ch08_deep` | 8장 딥러닝 |
| `common` | 여러 장에서 같이 쓰는 함수·계층 (functions.py, layers.py 등) |
| `dataset` | MNIST 데이터와 불러오는 코드 |
| `notes` | 공부 노트 (Obsidian `C:\Obsidian\DeepLearning`의 복사본 — `.\sync_notes.ps1`로 갱신, 여기서 직접 수정하지 않기) |

## 환경
- Python 3.13 가상환경: `.venv`
- 패키지 목록: `requirements.txt`

### 가상환경 켜기 (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

### 다른 PC에서 다시 만들기
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### GitHub에 올리기
```powershell
.\sync_notes.ps1
git add .
git commit -m "작업 내용"
git push
```

### 코드 실행
`C:\Deeplerning` 폴더에서 실행해야 `common`, `dataset`을 import할 수 있어요.
```powershell
python ch01_python\check_env.py
```
