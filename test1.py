s1 = int(input('Из какой системы: '))
p = int(input('Число: '))
n = len(str(p))
s2 = int(input('В какую систему: '))
result = 0
if s1<11 and s1!=10:
    for i in str(p):
        # print(result, n)
        result = result + s1**n * int(i)
        n = n-1
# print(result)
p = result
if s2<10:
    result = ""
    while p!=0:
        result = result + str(p%s2)
        p = p//s2
    print(result)
elif s2>10:
    result = ""
    while p!=0:
        if p%s2<10:
            result = result + str(p%s2)
            # p = p//s2
        elif p%s2>9:
            if p%s2==10:
                result = result + 'A'
            elif p%s2==11:
                result = result + 'B'
            elif p%s2==12:
                result = result + 'C'
            elif p%s2==13:
                result = result + 'D'
            elif p%s2==14:
                result = result + 'E'
            elif p%s2==15:
                result = result + 'F'
        p = p//s2
    result1 = []
    for g in result:
        result1.append(g)
    result1.reverse()
    result = ""
    for g1 in result1:
        result = result + g1
    print(result)
elif s2==10:
    print(result)
