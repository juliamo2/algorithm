# 递归求阶乘

n = int(input())


def factorial(n):
    if n <= 1:
        return 1
    else:
        s = factorial(n - 1)*n
        return s


print(factorial(n))
