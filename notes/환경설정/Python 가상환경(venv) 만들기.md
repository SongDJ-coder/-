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

관련: [[실습 폴더 구조]], [[VS Code 설정]]
