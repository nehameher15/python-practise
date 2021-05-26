#Calcualte checksum of number by doubling every 2nd digit from last
#1496= (1+1) + 4 + (1+8) + 6 = 21
def CalcChecksum(number):
    sum=otherdigit=secondPosdigit=0
    while(number>0):
        otherdigit=(int)(number%10)
        sum=sum+otherdigit
        secondPosdigit=(int)((number/10)%10)
        secondPosdigit+=secondPosdigit
        if(secondPosdigit>9):
            extractdigit=0
            extractdigit=(int)(secondPosdigit%10)
            secondPosdigit=(int)(secondPosdigit/10)
            sum=sum+extractdigit
            sum=sum+secondPosdigit
        else:
            sum=sum+secondPosdigit
        number=(int)(number/100)
    return sum
num=1496
result=CalcChecksum(num)
print(str(result) + " is Checksum")