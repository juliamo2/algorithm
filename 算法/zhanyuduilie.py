num = []
fh = []
s = input()

p1 = 0
p2 = 0

def yx(fh):
    if fh == '*' | '/':
        return 2
    elif fh == '+' | '-':
        return 1
    else:
        return -1


for i in s:
    if i >'0' | i < '9':
        num.append(i)
    else:
        while num & yx(i)<=yx(num[p1]):
            ans =
