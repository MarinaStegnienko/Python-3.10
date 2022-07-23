def sumNum3 (num):
    if num == 0:
        return 0
    if num % 9 ==0:
        return 9
    return num % 9

print(sumNum3(38))
print(sumNum3(40))
print(sumNum3(48))
print(sumNum3(2))
