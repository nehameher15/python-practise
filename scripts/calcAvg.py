#// p 0 - _ ) ? [ ]  { } ; :
def calculateAvg(numlist):
    try:
        sum=0
        for i in numlist:
            sum=sum+i
        a=sum/len(numlist)
        print("avg",a)
    except TypeError as e:
        print("TypeError", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError", e)
    finally:
        print("Finally")

num=[1,2,3,4,5]
calculateAvg(num)
num1=[]
calculateAvg(num1)
num2=[10,20,30,'abc']
calculateAvg(num2)