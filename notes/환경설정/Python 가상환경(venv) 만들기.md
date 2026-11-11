---
tags: [환경설정, python, venv]
작성일: 2026-11-08
---

# Python 가상환경(venv) 만들기

## 가상환경이 뭔가?
- 프로젝트마다 **따로 쓰는 파이썬 + 패키지 공간**.
- 여기에 설치한 NumPy 같은 패키지는 이 프로젝트에서만 쓰이고, 다른 프로젝트나 컴퓨터 전체에는 영향을 주지 않는다.
- 이 공부용 가상환경은 `C:\Deeplerning\.venv` 폴더에 있다.

## 1. 설치된 파이썬 확인
```powershell
py -0p
```
- 설치된 파이썬 버전 목록과 경로가 나온다.
- 내 PC에는 3.13, 3.14, 3.14t가 있다.
  - 3.14t는 실험용 버전이라 쓰지 않는다.
  - **3.13을 골랐다.** 라이브러리 호환성이 가장 안정적이기 때문이다.

## 2. 가상환경 만들기
```powershell
cd C:\Deeplerning
py -3.13 -m venv .venv
```
- `py -3.13`: 파이썬 3.13으로 실행한다.
- `-m venv .venv`: venv 모듈로 `.venv`라는 폴더에 가상환경을 만든다.

## 3. 가상환경 켜기 / 끄기
```powershell
.\.venv\Scripts\Activate.ps1   # 켜기 → 프롬프트 앞에 (.venv)가 붙는다
deactivate                     # 끄기
```
"스크립트를 실행할 수 없습니다" 오류가 나면 아래 명령을 **한 번만** 실행한다.
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
> 가상환경을 켜지 않고 `.\.venv\Scripts\python.exe 파일.py`처럼 가상환경 안의 파이썬을 직접 지정해서 실행해도 된다.

## 4. 패키지 설치
```powershell
python -m pip install --upgrade pip
python -m pip install numpy matplotlib jupyter ipykernel
```
| 패키지 | 용도 |
|---|---|
| numpy | 행렬 계산. 책 전체의 핵심 |
| matplotlib | 그래프 그리기 |
| jupyter, ipykernel | `.ipynb` 노트북에서 코드를 셀 단위로 실행 |

설치 당시 버전 (2026-11-08)
- Python 3.13.12
- NumPy 2.5.4
- matplotlib 3.11.2
- jupyter 1.1.1

## 5. requirements.txt — 설치 목록 저장하기
```powershell
python -m pip freeze > requirements.txt          # 지금 설치된 목록 저장
python -m pip install -r requirements.txt        # 목록대로 한 번에 설치
```
- 다른 PC나 새 가상환경에서도 같은 버전으로 다시 설치할 수 있다.
- `.venv` 폴더 자체는 GitHub에 올리지 않는다. 용량이 크고, 다른 PC에서는 동작하지 않기 때문이다. 대신 `requirements.txt`만 올린다.

## 6. 처음부터 다시 만들 때 (전체 순서)
```powershell
cd C:\Deeplerning
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
가상환경이 망가졌으면 `.venv` 폴더를 지우고 위 순서를 다시 실행하면 된다.

## 7. 제대로 됐는지 확인
```powershell
python ch01_python\check_env.py
```
- 파이썬·NumPy·matplotlib 버전이 출력된다.
- 행렬 계산 결과가 출력된다.
- `ch01_python\check_env.png`에 sin·cos 그래프가 저장된다.

## 8. 직접 해 보며 겪은 실수 (2026-11-11)
### `python -m venv`로 만들었더니 3.14가 됐다
- `python`을 그냥 치면 컴퓨터 기본 파이썬(3.14)이 실행된다.
- 원하는 버전은 반드시 `py -3.13`처럼 직접 지정한다.
- `py -0p` 목록의 `*` 표시가 기본 버전이다. 내 PC는 3.14t(실험용)가 기본이다.
- 어떤 파이썬이 실행됐는지는 에러 메시지 맨 앞의 경로나 아래 파일로 확인한다.
  ```powershell
  cat .venv\pyvenv.cfg   # version = 3.13.x 인지 확인
  ```

### 오타: `venu`
```
No module named venu
```
모듈 이름을 잘못 쳤다는 뜻이다. `venv`가 맞다.

### 가상환경을 다시 만들기
```powershell
deactivate                          # 1. 켜져 있으면 먼저 나가기
py -3.13 -m venv --clear .venv      # 2. --clear: 기존 내용을 비우고 새로 만들기
```
- 켜진 상태로 다시 만들면 터미널이 지워진 환경을 가리키는 꼬인 상태가 될 수 있다.
- `--clear` 대신 `Remove-Item -Recurse -Force .venv`로 지워도 된다. 이 명령은 휴지통을 거치지 않으니 주의한다.

### `pip install -r requirements.txt`를 했더니 `Requirement already satisfied`가 나왔다
- 이미 다 설치돼 있다는 뜻이다. 정상이다.
- 이 명령은 **새 PC나 새 가상환경**에서 쓰는 용도다.

### 설치 중 `Using cached ...`
- 예전에 받아 둔 파일을 재사용한다는 뜻이다. 정상이다.

### 노트북에서 커널이 안 잡혔다
- 터미널에서 가상환경을 켠 것과 노트북 커널은 **따로** 정해진다.
- 노트북에서 직접 골라 줘야 한다: `Select Kernel` → `Python Environments...` → `.venv (3.13.x)`
- 자세한 내용은 [[VS Code 설정]] 참고.

## 9. 처음부터 다시 만들기 (2026-11-11 연습)
`C:\Deeplerning`을 완전히 비우고 1~7번을 직접 다시 했다. 장별 폴더(`ch01_python` ~ `ch08_deep`, `common`, `dataset`)와 각 장의 빈 노트북(`ch01.ipynb` 등)을 만들었다.
- `.vscode\settings.json`, `.gitignore`, Git 연결은 아직 다시 하지 않았다.

관련: [[실습 폴더 구조]], [[VS Code 설정]]
