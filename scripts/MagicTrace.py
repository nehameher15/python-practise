#// p 0 - _ ) ? [ ]  { } ; :
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