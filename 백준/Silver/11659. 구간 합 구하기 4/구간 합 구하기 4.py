import sys
input=sys.stdin.readline

n,m=map(int,input().split( ))
lst=list(map(int,input().split( )))
new_lst=[0]
start=0
for a in lst:
    start+=a
    new_lst.append(start)
# print(new_lst)

for _ in range(m): # m만큼 반복
    i,j=map(int,input().split( ))
    print(new_lst[j]-new_lst[i-1])