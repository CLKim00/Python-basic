# -*- coding: utf-8 -*-
"""Matplotlib 라이브러리를 활용한 가시화_class101_데이터 마이닝.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NrAZD-rsev1-H7_fz_ooStQEsMrceiCz

### matplotlib : 디자인감각 필요, 커스터마이징하기 용이함
### seaborn : 자동으로 예쁜 그림을 그려주지만, 커스터마이징이 자유롭지 않음
### pandas : 간단한 그래프를 그릴 때 주로 활용
"""

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
tips

fig = plt.figure()    # 흰색 도화지
ax = fig.add_subplot(1, 1, 1)

ax.hist(tips['total_bill'], bins = 20)    # 다시 실행 시 덧칠
ax.set_title("Histogram")
ax.set_xlabel("total bill")
ax.set_ylabel("freq")

fig

plt.scatter(tips['total_bill'],    # 한 개만 그릴 시 자리 할당 필요X
            tips['tip'], 
            s = tips['size'] * 10, # 점 사이즈
            c = tips['size'],      # 점 색깔
            alpha = 0.5)           # 투명도

"""### 다른 데이터프레임을 가져와서 matplotlib 라이브러리를 통해 그림을 그리고 인증하기"""

mpgs = sns.load_dataset("mpg")
mpgs

mpgs = sns.load_dataset("mpg")
mpgs

fig2 = plt.figure() 
ax2 = fig.add_subplot(1, 1, 1)

plt.scatter(mpgs['acceleration'],
            mpgs['mpg'],
            c = mpgs['weight'])

