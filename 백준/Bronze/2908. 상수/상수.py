a,b=input().split()
# print(a,b)
WHAT=a
for i in range(2,-1,-1):
    if a[i]>b[i]:
        print(a[::-1])
        break
    elif b[i]>a[i]:
        # WHAT=b
        print(b[::-1])

        break
    else:
        continue

