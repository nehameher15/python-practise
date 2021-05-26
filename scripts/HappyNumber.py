#// p 0 - _ ) ? [ ]  { } ; :
def isHappyNumber(number):
    rem=sum=0
    while(number>0):
        rem=(int)(number%10)
        #print(rem)
        sum=sum+(rem*rem)
        #print(sum)
        number=(int)(number/10)
        #print(number)
    #print(sum)
    return sum
num=[31,32]
#result=num
sum=0
for i in num:
    result=i
    while(result !=1 and result !=4):
        result=isHappyNumber(result)
        print(result)
    if(result==1):
        sum=sum+i
        print(sum)
print(str(sum) + " sum of happy numbers")






