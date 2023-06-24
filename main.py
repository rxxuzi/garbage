import math

for i in range(2, 11):
    # Rounded down to the second decimal place
    nishiyama = round(math.log(2, i), 2)
    # print(nishiyama)
    # print(i)

e = 0.001


# function about x^2
def f(x):
    return x**3 + math.sin(x) * 10


# 微分
def differential(x):
    return (f(x + e) - f(x)) / e


# 　fx の積分
def integral(a, b):
    x = a
    n = 0
    cnt = 0
    while x < b:
        y = f(x)
        n += y * e
        cnt += 1
        if cnt % 10 == 0:
            s = "x : " + str(x) + ", y : " + str(y) + ", n : " + str(n)
            # print(s)

        x += e

    return n


print("df(0) : " + str(differential(0)))
a = 0
b = 10
print(f"f(x) [{a} -> {b}]: " + str(integral(0, 10)))
