number = int(input("insert number for elements "))
a=0
lst=[]
while a<number :

    x=int(input("insert : "))
    lst.append(x)
    a+=1

n = len(lst)
for i in range(0,n-1,2):
    lst[i],lst[i+1] = lst[i+1],lst[i]
print(lst)
