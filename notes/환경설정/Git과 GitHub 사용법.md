---
tags: [환경설정, git, github]
작성일: 2026-11-08
---

# Git과 GitHub 사용법

- 레포: https://github.com/SongDJ-coder/- (공개)
- 레포에 연결된 로컬 폴더: `C:\Deeplerning`
- 올리는 것
  - 실습 코드 (`ch01_python` ~ `ch08_deep`, `common`, `dataset`)
  - 정리 노트 (`notes\`) — Obsidian 폴더 `C:\Obsidian\DeepLearning`을 복사한 것

## 용어
| 용어 | 뜻 |
|---|---|
| 레포(repository) | Git이 관리하는 프로젝트 폴더 |
| 커밋(commit) | 지금 상태를 기록으로 남기는 것 (세이브 포인트) |
| 푸시(push) | 내 PC의 커밋을 GitHub로 올리는 것 |
| 풀(pull) | GitHub의 변경을 내 PC로 받아오는 것 |
| 원격(remote), `origin` | 연결된 GitHub 레포의 별명 |
| 브랜치(branch) | 작업 갈래. 기본은 `main` |

## 처음 한 번만 하는 설정
```powershell
git config --global user.name "Song Dongjun"
git config --global user.email "내 이메일"
gh auth login        # GitHub CLI 로그인 (브라우저로 인증)
```

## 레포 연결 (2026-11-08에 한 작업)
```powershell
cd C:\Deeplerning
git init -b main                                           # Git 레포로 만들기, 기본 브랜치 main
git remote add origin https://github.com/SongDJ-coder/-.git  # GitHub 레포 연결
git add .                                                  # 모든 변경 담기
git commit -m "환경 설정과 폴더 구조"                        # 기록 남기기
git push -u origin main                                    # 올리기 (-u: 다음부터 git push만 써도 됨)
```

## Git이 동작하는 방식 (세 공간 + GitHub)
```
① 작업 폴더 ──git add──▶ ② 스테이징 ──git commit──▶ ③ .git (내 PC) ──git push──▶ ④ GitHub
                                                                  ◀──git fetch/pull──
```
- `.git` 폴더는 파일 복사본이 아니라 **사진첩**이다. 커밋할 때만 그 순간 상태를 압축해서 저장한다.
- 바뀌지 않은 파일은 다시 저장하지 않는다.
- `.gitignore`에 적은 파일은 Git이 아예 보지 않는다.
- Git은 **빈 폴더를 추적하지 않는다.** 그래서 빈 폴더에는 `.gitkeep`이라는 빈 파일을 넣어 둔다.
- `git` 명령은 가상환경이 켜져 있든 꺼져 있든 상관없다. 파이썬과 별개의 프로그램이다.

## 이미 커밋이 있는 레포에 다시 연결하기 (2026-11-11에 직접 함)
로컬 폴더를 비우고 새로 만들었는데 GitHub에는 예전 커밋이 남아 있는 상황이다. 이때 그냥 push하면 기록이 이어지지 않아서 거절된다.
```powershell
git init -b main
git remote add origin https://github.com/SongDJ-coder/-.git
git fetch origin            # GitHub 기록만 받아 옴 (내 파일은 안 바뀜)
git reset origin/main       # 내 main을 GitHub 마지막 커밋에 맞춤 (파일은 그대로) ※ --hard 금지
git status                  # deleted / modified / untracked 확인
git restore 살릴파일 ...     # 지워진 파일 중 살릴 것 되살리기 (커밋 전에만 가능)
git add .
git commit -m "메시지"
git push -u origin main     # -u: 처음 한 번만. 이후엔 git push
```
- `git status`의 `deleted`는 마지막 커밋에는 있는데 지금 폴더에는 없는 파일이다.
- `modified`는 내용이 바뀐 파일, `Untracked`는 Git이 처음 보는 파일이다.
- 내가 한 실수: `origin/main`을 `origin.main`으로 쳐서 `ambiguous argument` 에러가 났다. `Tab` 자동 완성을 쓰면 오타를 줄일 수 있다.
- `No commits yet`이 나오면 아직 reset이 안 된 상태다.

## 한글 파일 이름이 `\355\231...`로 보일 때
```powershell
git config --global core.quotepath false
```

## PowerShell에서 한글이 깨질 때 (`cat`)
- 파일은 UTF-8로 정상 저장돼 있다. PowerShell 5.1이 CP949로 잘못 읽어서 깨져 보이는 것이다.
- `cat 파일 -Encoding utf8`로 읽으면 제대로 보인다.
- 매번 붙이기 싫으면 `$PROFILE`에 `$PSDefaultParameterValues['*:Encoding'] = 'utf8'`을 추가한다.

## .gitignore — 올리지 않을 파일 목록
```
.venv/            가상환경 (requirements.txt로 다시 만들 수 있음)
__pycache__/      파이썬 캐시
dataset/*.gz      MNIST 데이터 (용량 큼)
dataset/*.pkl
.obsidian/        Obsidian 설정
```

## 평소에 올리는 순서 ⭐
```powershell
cd C:\Deeplerning
.\sync_notes.ps1               # 1. Obsidian 노트를 notes\로 복사
git status                     # 2. 무엇이 바뀌었는지 확인
git add .                      # 3. 변경 담기
git commit -m "3장 p.40-55"    # 4. 무슨 작업인지 메시지 남기기
git push                       # 5. GitHub에 올리기
```

`sync_notes.ps1`은 Obsidian 폴더를 `notes\`와 똑같이 맞춘다.
- Obsidian에서 지운 노트는 `notes\`에서도 지워진다.
- **노트는 항상 Obsidian에서 수정한다.** `notes\`에서 직접 고치면 다음 동기화 때 덮어써진다.

## 자주 쓰는 명령
| 명령 | 기능 |
|---|---|
| `git status` | 바뀐 파일 보기 |
| `git log --oneline` | 커밋 기록 보기 |
| `git diff` | 바뀐 내용 자세히 보기 |
| `git pull` | GitHub의 최신 내용 받기 (다른 PC에서 작업했을 때) |
| `git restore 파일` | 커밋 안 한 변경 되돌리기 (주의: 되돌린 내용은 사라짐) |

## 다른 PC에서 받아서 시작하기
```powershell
git clone https://github.com/SongDJ-coder/-.git Deeplerning
cd Deeplerning
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## VS Code에서 하기
1. 왼쪽 **소스 제어** 아이콘(`Ctrl+Shift+G`)을 누른다. 바뀐 파일이 보인다.
2. 파일 옆 `+`를 누른다. `git add`와 같다.
3. 메시지를 입력하고 **커밋**을 누른다.
4. **변경 내용 동기화**를 누른다. push와 pull이 함께 된다.

관련: [[Python 가상환경(venv) 만들기]], [[VS Code 설정]], [[실습 폴더 구조]]
