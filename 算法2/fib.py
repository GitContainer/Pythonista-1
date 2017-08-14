# 递归
def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


# 非递归
def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a


# 0 1 1 2 3 5 8 13 21 55
# 0 1 2 3 4 5 6 7 8 9 10
print(fib1(10))
print(fib2(10))
