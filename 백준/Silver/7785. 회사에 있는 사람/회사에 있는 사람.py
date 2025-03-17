n=int(input())
record={}
for _ in range(n):
    a,b=input().split()
    record[a]=b

lst=[]
for key,val in record.items():
    if val=='enter':
        lst.append(key)
sorted_lst=sorted(lst,reverse=True)

for _ in sorted_lst:
    print(_)