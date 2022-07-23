def sumNum(num):
    return 0 if not num else num % 10 + sumNum(num // 10)
num = abs(int(input()))
while num > 9:
    num = sumNum(num)
print(num)
sumNum(48)