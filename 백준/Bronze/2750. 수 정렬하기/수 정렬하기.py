n=int(input())
a=[0]*n
# print(a)
for _ in range(n):
    a[_]=int(input())
# print(a)

for i in range(n):
    for j in range(i,n):
        if a[j]<a[i]:
            # print(i,j)
            a[i],a[j]=a[j],a[i]
            # small=a[j]
            # big=a[i]
            # a[j]=big
            # a[i]=small
            # print(a)

for k in a:
    print(k)
