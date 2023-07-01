import math

for i in range(2, 11):
    log2 = math.log(i, 2)
    nishiyama = round(log2)
    print(f"log2({i}) = {nishiyama}")

function = input("function: ")

def f(x):
    return x * x

