k=int(input())

wallet=[]
for i in range(k):
    a=int(input())
    if a!=0:
        wallet.append(a)
    else:
        wallet.pop()

print(sum(wallet))