import matplotlib.pyplot as plt
import numpy as np

# -10에서 10까지의 범위안에 균등하게 간격을 두어 100개의 값(데이터)를 생성해봐
x = np.linspace(-10,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.show()

def not_used4():
# 연습
# x의 범위가 -10에서 10일떄 x의 제곱을 그려 봅니다.
    x = np.arange(-10,10,0.1)
    y = x ** 2
    plt.plot(x,y,'ro')
    plt.show()

def not_user3():
    y = []
    x = list(range(-10,11,1))
    for a in x:
        y.append(a**2)
    plt.plot(x, y, 'ro')
    plt.show()

# x = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
# y = []
    # for i in range(len(x)):
    #     j = (x[i]*x[i])
    #     y.append(j)
    # plt.plot(x, y,'ro')
    # plt.show()

def not_used2():
    age = [28,16,40,30,20,29,28,27]
    height = [175,180,173,167,188,157,169,177]
    plt.plot(age, height)
    plt.show()

def not_user():
    data = [28,16,40,30,20,29,28,27]
    plt.plot(data)
    plt.show()

