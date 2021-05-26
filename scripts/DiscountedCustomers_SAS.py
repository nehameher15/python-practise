#Return names of customers who bought products always at discounted price
import operator
'''
Rajan Patil, Aundh, 1, Phone Cover, Rs 170, Cash
Mohit Gupta, Baner, 1, Samsung Battery, Rs 900, Credit Card
Rajan Patil, Aundh, 3, Samsung Battery, Rs 1000, Cash
Nina Kothari, Baner, 4, Earphones, Rs 500, Credit Card
T Sunitha, Shivajinagar, 5, Earphones, Rs 550, Credit Card
Rohan Gade, Aundh, 10, Motorola Battery, Rs 1000, Credit Card
Rajan Patil, Shivajinagar, 21, Earphones, Rs 550, Credit Card
Rajan Patil, Aundh, 22, USB Cable, Rs 150, UPI
Meena Kothari, Baner, 23, USB Cable, Rs 100, Cash
Nina Kothari, Baner, 24, USB Cable, Rs 200, UPI
Mohit Gupta, Baner, 25, USB Cable, Rs 150, UPI
'''
def CalcDiscntdCustomers():
    f = open('D:\python-practise-dev-github\python-practise\input_data\Customers_List.txt')
    lines=[]
    Proddict= {}
    maxlist=[]
    discountedlist=[]
    for line in f:
        lines.append(line)
    f.close()
    for P in lines:
        x=P.split(',').__getitem__(3).strip()
        val=(int)(P.split(',').__getitem__(4).replace(" Rs ",''))
        if x in Proddict:
            Proddict[x].append((int)(val))
        else:
            Proddict[x]=[(int)(val)]
        items=Proddict[x]
        items.sort(reverse=True)
        Proddict[x]=items
    for custProd in lines:
        Prodname = (custProd.split(',').__getitem__(3).strip())
        ProdPrice = (int)(custProd.split(',').__getitem__(4).replace(" Rs ", ''))
        if (len(Proddict[Prodname]) > 1):
            if (ProdPrice.__eq__(Proddict[Prodname].__getitem__(0))):
                maxlist.append(custProd.split(',').__getitem__(0).strip())
            elif (ProdPrice.__le__(Proddict[Prodname].__getitem__(0))):
                discountedlist.append(custProd.split(',').__getitem__(0).strip())
    for d in set(discountedlist):
        if (not set(maxlist).__contains__(d)):
            print(d)
if __name__ == '__main__':
    CalcDiscntdCustomers()
