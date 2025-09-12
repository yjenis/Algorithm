from collections import deque
n,l=map(int,input().split( ))
numbers=list(map(int,input().split( )))
windows=deque()

for i in range(n):
    while windows and windows[-1][0]>numbers[i]:
        # print(windows[-1][0],numbers[i])
        windows.pop()
    windows.append((numbers[i],i))

    if windows[0][1]<=i-l:
        windows.popleft()
    print(windows[0][0],end=" ")