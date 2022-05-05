n = int(input())


def fibonacci5(n):
    def fn(i):
        if i < 2:
            return 1
        else:
            return fn(i - 2) + fn(i - 1)

    for i in range(n):
        print(fn(i))


fibonacci5(n)