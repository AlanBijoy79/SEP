amount = int(input("Enter the amount you want to withdraw: "))
l=[2000,500,200,100,50,20,10,5,2,1]
for i in l:
    count=amount//i
    amount=amount%i
    if count>0:
        print ("Number of denominations of ",i," is ",count)

