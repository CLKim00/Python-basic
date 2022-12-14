# -*- coding: utf-8 -*-
"""Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EVOEcqPjbxz7g2cfOVMr_m5d4Wyqkj4x

# 1. Numpy란?
"""

# numpy 사용하기
import numpy as np

"""# 2. Array 정의 및 사용"""

data1 = [1, 2, 3, 4, 5]
data1

data2 = [1, 2, 3, 3.5, 4]
data2

# numpy를 이용해 array 정의하기
# 위에서 만든 python list 이용
arr1 = np.array(data1)
arr1

# array의 형태(크기) 확인
arr1.shape

# python list를 직접 입력
arr2 = np.array([1, 2, 3, 4, 5])
arr2

arr2.shape

# array 자료형 확인
arr2.dtype

arr3 = np.array(data2)
arr3

arr3.shape

arr3.dtype

arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
arr4

arr4.shape

"""## 2-1. np.zeros(), np.ones(), np.arange() 함수
numpy에서 array를 정의할 때 사용되는 함수
"""

# np.zeros() 함수는 인자로 받는 크기만큼, 모든 요소가 0인 array를 만든다.
np.zeros(10)

np.zeros((3, 5))

# np.ones() 함수는 인자로 받는 크기만큼, 모든 요소가 1인 array를 만든다.
np.ones(9)

np.ones((2, 10))

# np.arange() 함수는 인자로 받는 값만큼 1씩 증가하는 1차원 array를 만든다.
# 이때 하나의 인자만 입력하면 0 ~ 입력한 인자, 값만큼의 크기를 가진다.
np.arange(10)

np.arange(3, 10)

"""# 3. Array 연산
numpy의 연산은 크기가 동일한 array끼리 연산이 진행된다. 이 때 같은 위치에 있는 요소들끼리 연산이 된다.
"""

arr1 = np.array([[1, 2, 3],[4, 5, 6]])
arr1

arr1.shape

arr2 = np.array([[10, 11, 12],[13, 14, 15]])
arr2

arr2.shape

"""## 3-1. Array 덧셈"""

arr1 + arr2

"""## 3-2. Array 뺄셈"""

arr1 - arr2

"""## 3-3. Array 곱셈"""

arr1 * arr2

"""## 3-4. Array 나눗셈"""

arr1 / arr2

"""## 3-5. Array의 브로드 캐스트
브로드캐스트란, 서로 크기가 다른 array의 연산을 제공한다.
"""

arr1

arr1.shape

arr3 = np.array([10, 11, 12])
arr3

arr3.shape

arr1 + arr3

arr1 * arr3

# 위와 같이 서로 크기가 다른 arr1과 arr3의 연산이 가능하다.
# 연산 결과를 살펴보면 arr3가 [10,11,12]에서 [[10,11,12],[10,11,12]]로 확장되어 계산되었음을 확인할 수 있다.

# 동일한 방식으로 하나의 array에 스칼라 연산도 가능하다.

arr1 * 10

# 요소에 대해 제곱처리
arr1 ** 2

"""# 4. Array 인덱싱
numpy의 인덱싱은 python의 인덱싱과 동일하지만 1번째에서 시작하는 것이 아니라 0번째에서 시작하는 것에 주의한다.
"""

arr1 = np.arange(10)
arr1

# 0번째 요소
arr1[0]

# 3번째 요소
arr1[3]

# 3번째 요소부터 8번째 요소
arr1[3:9]

arr1[:]

# 1차원 이상의 인덱싱

arr2 = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
arr2

# 2차원의 array의 인덱싱은 2개의 인자 입력
arr2[0,0]

# 2행의 모든 요소
arr2[2,:]

# 2행의 3번째 요소
arr2[2,3]

# 모든 행의 3번째 요소
arr2[:,3]

"""# 5. Array boolean 인덱싱(마스크)
위에서 이용한 다차원 인덱싱을 응용해 boolean 인덱싱을 할 수 있다. 해당 기능은 주로 마스크라고 이야기하는데, boolean 인덱싱을 통해 만들어낸 array를 통해 우리가 원하는 행 또는 열의 값만 뽑아낼 수 있다. 즉, 마스크처럼 우리가 가리고 싶은 부분은 가리고, 원하는 요소만 꺼낼 수 있다.
"""

names = np.array(['Beomwoo', 'Beomwoo', 'Kim', 'Joan', 'Lee', 'Beomwoo', 'Park', 'Beomwoo'])
names

names.shape

# 아래에서 사용되는 np.random.randn() 함수는 기대값이 0이고, 표준편차가 1인 가우시안 정규 분포를 따르는 난수를 발생시키는 함수
# 이 외에도 0~1의 난수를 발생시키는 np.random.rand() 함수도 존재

data = np.random.randn(8,4)
data

data.shape

# names의 각 요소가 data의 각 행과 연결된다고 가정해보자.
# 그리고 이 때, names가 Beomwoo인 행의 data만 보고 싶을 때 다음과 같이 마스크를 사용한다.

# 요소가 Beomwoo인 항목에 대한 mask 생성
names_Beomwoo_mask = (names == 'Beomwoo')
names_Beomwoo_mask

data[names_Beomwoo_mask,:]    # 요소가 Beomwoo인 것에 대한 boolean값을 가지는 mask를 인덱싱에 응용하여 data의 0,1,5,7행을 꺼냄

# 요소가 Kim인 행의 데이터만 꺼내기
data[names == 'Kim',:]

# 논리 연산을 응용해 요소가 Kim 또는 Park인 행의 데이터만 꺼내기
data[(names == 'Kim') | (names == 'Park'),:]

# data array 자체적으로도 마스크를 만들고 응용하여 인덱싱이 가능하다.
# data array에서 0번째 열의 값이 음수인 행을 구해보자.

# 마스크 만들기
# data array에서 0번째 열이 음수인 요소의 boolean값은 다음과 같다.
data[:,0] < 0

# 만든 마스크를 이용해 0번째 열이 음수인 행 구하기
data[data[:,0]<0,:]

# 특정 위치에 원하는 값 대입하기

# 0번째 열의 값이 음수인 행의 2,3번째 열의 값
data[data[:,0]<0,2:4]

data[data[:,0]<0,2:4] = 0
data

"""# 6. Numpy 함수

## 6-1. 하나의 array에 적용되는 함수
"""

arr1 = np.random.randn(5,3)
arr1

# 각 성분의 절대값 계산
np.abs(arr1)

# 각 성분의 제곱근 계산 ( == array ** 0.5)
np.sqrt(arr1)

# 각 성분의 제곱 계산
np.square(arr1)

# 각 성분을 무리수 e의 지수로 삼은 값 계산
np.exp(arr1)

# 각 성분을 자연로그, 상용로그, 밑이 2인 로그를 씌운 값 계산
np.log(arr1)

np.log10(arr1)

np.log2(arr1)

# 각 성분의 부호 계산 (+인 경우는 1, -인 경우는 -1, 0인 경우는 0)
np.sign(arr1)

# 각 성분의 소수 첫 번째 자리에서 올림한 값 계산
np.ceil(arr1)

# 각 성분의 소수 첫 번째 자리에서 내림한 값 계산
np.floor(arr1)

# 각 성분이 NaN인 경우 True, 아닌 경우 False 반환
np.isnan(arr1)

np.isnan(np.log(arr1))

# 각 성분이 무한대인 경우 True, 아닌 경우 False 반환
np.isinf(arr1)

# 각 성분에 대해 삼각함수 값을 계산 (cos, cosh, sin, sinh, tan, tanh)
np.cos(arr1)

np.tanh(arr1)

"""## 6-2. 두 개의 array에 적용되는 함수"""

arr1

arr2 = np.random.randn(5, 3)
arr2

# 두 개의 array에 대해 동일한 위치의 성분끼리 연산 값 게산(add, subtract, multiply, divide)
np.multiply(arr1, arr2)

# 동일한 위치의 성분끼리 비교해 최대값 또는 최소값 계산(maximum, minimum)
np.maximum(arr1, arr2)

"""## 6-3. 통계 함수
통계 함수를 통해 array의 합이나 평균 등을 구할 때 추가로 axis라는 인자에 대한 값을 지정하여 열 또는 행의 합 또는 평균 등을 구할 수 있다.
"""

arr1

# 전체 성분의 합
np.sum(arr1)

# 열 간의 합
np.sum(arr1, axis = 1)

# 행 간의 합
np.sum(arr1, axis = 0)

# 전체 성분의 평균
np.mean(arr1)

# 행 간의 평균
np.mean(arr1, axis = 0)

# 전체 성분의 표준편차, 분산, 최소값, 최대값 계산(std, var, min, max)
np.std(arr1)

np.min(arr1, axis = 1)

# 전체 성분의 최소값, 최대값이 위치한 인덱스를 반환(argmin, argmax)
np.argmin(arr1)    # 모든 원소를 1차원 array에 편 상태를 가정하고, argmax를 적용한 결과를 반환

np.argmax(arr1, axis = 1)    # 가로 축 원소들끼리 비교하여 각 가로축 내부에서 argmax를 각각 적용

np.argmax(arr1, axis = 0)    # 세로 축 원소들끼리 비교하여 각 세로축 내부에서 argmax를 각각 적용

# 맨 처음 성분부터 각 성분까지의 누적합 또는 누적곱 (cumsum, cumprod)
np.cumsum(arr1)

np.cumsum(arr1, axis = 1)

np.cumprod(arr1)

"""## 6-4. 기타 함수"""

arr1

# 전체 성분 오름차순 정렬
np.sort(arr1)

# 전체 성분 내림차순 정렬
np.sort(arr1)[::-1]

# 행 방향으로 오름차순 정렬
np.sort(arr1, axis = 0)

