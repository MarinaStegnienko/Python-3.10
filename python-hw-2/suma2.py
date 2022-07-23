def sumNum2(num):
    tmpRes=0
    while num >0:
        tmpRes += num % 10
        num = num // 10

        if num ==0 and tmpRes > 9:
            num = tmpRes
            tmpRes = 0
    return tmpRes

sumNum2(48)