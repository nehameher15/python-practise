#Calculate sum of beautiful/happy numbers
def isHappyNumber(number):
    rem=sum=0
    while(number>0):
        rem=(int)(number%10)
        sum=sum+(rem*rem)
        number=(int)(number/10)
    return sum
num=[31,32]
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






