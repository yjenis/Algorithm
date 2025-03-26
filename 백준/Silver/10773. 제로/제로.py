k=int(input())

wallet=[]
for i in range(k):
    a=int(input())
    if a==0:
        wallet.pop()
    else:
        wallet.append(a)

print(sum(wallet))