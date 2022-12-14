# -*- coding: utf-8 -*-
"""함수에 대한 이해와 함수 만들기_class101_데이터 마이닝.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vFhMzC-LpG6Us2-YycZtFWlveOFJM7nf
"""

# def 함수이름(재료):

def add(num1, num2):
    return num1 + num2

a = add(3, 5)
a

# 매개변수가 없는 경우
def say():
    return 'hello'

a = say()
a

# 반환값이 없는 경우
def add(num1, num2):
    print(num1 + num2)

# 함수 내의 print 출력
a = add(3, 4)

# 함수의 반환값이 없으므로 None
print(a)

def test1(x):
    return x > 0

test1(5)

test1(-5)

def intro(name, age, sex=5):
    print('나의 이름은 {}이고, {}살입니다.'.format(name, age))
    if sex == 5:
        print('나는 남자입니다.')
    else:
        print('나는 여자입니다.')

intro('홍길동', 30)

intro('장원영', 19, 3)

def test():
    a = 5    # 지역변수

a = 0    # 전역변수
test()
print(a)

def test():
    global a    # 전역변수 선언
    a = 5

a = 0
test()
print(a)

# 재귀함수

def fac(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    return a

fac(5)

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

fac(5)

"""# 직각삼각형의 밑변의 길이, 높이의 길이를 넣어주면, 빗변의 길이를 반환하는 함수를 만들어보세요."""

def pythagoras(a, b):
    return (a**2 + b**2) ** (1/2)

pythagoras(2, 3)

