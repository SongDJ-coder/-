"""환경 점검용 스크립트: NumPy 계산과 matplotlib 그래프가 되는지 확인한다."""
import os
import sys

import matplotlib
import numpy as np

print("Python    :", sys.version.split()[0])
print("NumPy     :", np.__version__)
print("matplotlib:", matplotlib.__version__)

# NumPy 브로드캐스트와 행렬 곱 (1장 내용 맛보기)
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print("A * B  =\n", A * B)
print("A @ A  =\n", A @ A)

# sin, cos 그래프를 그려서 파일로 저장
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
plt.plot(x, np.sin(x), label="sin")
plt.plot(x, np.cos(x), linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()

out = os.path.join(os.path.dirname(__file__), "check_env.png")
plt.savefig(out)
print("그래프 저장:", out)
