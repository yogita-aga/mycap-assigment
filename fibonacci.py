num=int(input("Enter a number:"))
n1,n2=0,1
sum=0
if num<=0:
    print("Enter a number greater than 0")
else:
    for i in range(0,num):
        print(sum)
        n1=n2
        n2=sum
        sum=n1+n2
