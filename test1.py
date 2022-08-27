p = int(input('Число: '))
s = int(input('В какую систему?: '))
result = ""
while p!=0:
    result = result + str(p%s)
    p = p//s
print(result)
