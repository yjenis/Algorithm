import heapq

N=int(input())
pq=[]
for _ in range(N):
    pq.append(int(input()))


pq.sort()


total=0
while len(pq)>1:
    temp=0
    a=heapq.heappop(pq)
    b=heapq.heappop(pq)
    temp+=a
    temp+=b
    heapq.heappush(pq,temp)
    total+=temp

print(f'{total}')