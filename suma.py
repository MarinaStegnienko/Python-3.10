def sumNum(num):
    sum = 0
    while num>0:
        sum += num%10
        num //= 10
    return sum
 
num = int(input())
while num>9:
    num = sumNum(num)
print(num)