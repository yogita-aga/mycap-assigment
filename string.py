str=input("Please enter a string: ")
count={}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
print(count)
