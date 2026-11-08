---
tags: [환경설정, vscode]
작성일: 2026-11-08
---

# VS Code 설정

## 폴더 열기
- VS Code → `파일 > 폴더 열기` → `C:\Deeplerning` 선택
- 또는 터미널에서 아래 명령을 실행한다.
  ```powershell
  code C:\Deeplerning
  ```

## 필요한 확장 (Extensions, `Ctrl+Shift+X`)
- **Python** (Microsoft)
- **Jupyter** (Microsoft) — `.ipynb` 노트북용

## 프로젝트 설정 파일: `.vscode/settings.json`
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true,
  "terminal.integrated.env.windows": {
    "PYTHONPATH": "${workspaceFolder}"
  }
}
```
| 설정 | 의미 |
|---|---|
| `python.defaultInterpreterPath` | 이 폴더에서는 `.venv`의 파이썬을 쓴다 |
| `python.terminal.activateEnvironment` | 터미널을 열면 가상환경이 자동으로 켜진다 |
| `PYTHONPATH` | 어느 폴더에서 실행하든 `common`, `dataset`을 import할 수 있다 |

> `${workspaceFolder}`는 VS Code에서 연 폴더, 즉 `C:\Deeplerning`을 뜻한다.

## 인터프리터가 안 잡힐 때
1. `Ctrl+Shift+P`를 누른다.
2. `Python: Select Interpreter`를 고른다.
3. `.venv` 항목을 선택한다.

오른쪽 아래 상태 표시줄에 `3.13.x ('.venv')`가 보이면 정상이다.

## 자주 쓰는 단축키
| 단축키 | 기능 |
|---|---|
| `Ctrl+`` ` | 터미널 열기/닫기 |
| `F5` | 현재 파일 디버그 실행 |
| `Ctrl+F5` | 디버그 없이 실행 |
| `Ctrl+Shift+P` | 명령 팔레트 |
| `Ctrl+/` | 주석 토글 |
| `Shift+Enter` | (노트북) 셀 실행 후 다음 셀로 이동 |

관련: [[Python 가상환경(venv) 만들기]], [[실습 폴더 구조]]
