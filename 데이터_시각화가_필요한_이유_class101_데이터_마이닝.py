# -*- coding: utf-8 -*-
"""데이터 시각화가 필요한 이유_class101_데이터 마이닝.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eBMaEsNn6dsRFal1IC0Fi7CxSrGIc991

# matplotlib : 그래프를 그려주는 라이브러리
# seaborn : 데이터분석연습 라이브러리 + 가시화
"""

import matplotlib.pyplot as plt
import seaborn as sns

anscombe = sns.load_dataset("anscombe")
anscombe

data1 = anscombe[anscombe['dataset'] == 'I']
data2 = anscombe[anscombe['dataset'] == 'II']
data3 = anscombe[anscombe['dataset'] == 'III']
data4 = anscombe[anscombe['dataset'] == 'IV']

data1

data2

data3

data4

print(data1.mean())
print(data2.mean())
print(data3.mean())
print(data4.mean())

print(data1.std())
print(data2.std())
print(data3.std())
print(data4.std())

fig = plt.figure()    # 흰색 도화지

ax1 = fig.add_subplot(2, 2, 1)    # 2행 2열 1자리
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.scatter(data1['x'], data1['y'])    # 산점도
ax2.scatter(data2['x'], data2['y']) 
ax3.scatter(data3['x'], data3['y']) 
ax4.scatter(data4['x'], data4['y']) 

fig

ax1.set_title("data1")    # .set_title(): 그림의 제목
ax2.set_title("data2")
ax3.set_title("data3")
ax4.set_title("data4")

fig

fig.suptitle("Anscombe Data")    # .suptitle(): 메인 도화지의 제목
fig

fig.tight_layout()    # .tight_layout(): 그림에서 겹쳐서 맞지 않는 레이아웃 정돈
fig

