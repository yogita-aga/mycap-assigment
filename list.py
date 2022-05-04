list1=[12,-7,5,64,-14]
print(list1)
i=0
for e in range(len(list1)):
    if list1[i]<0:
        del list1[i]
    else:
        i+=1
print(list1)

