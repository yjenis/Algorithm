import sys
def input(): return sys.stdin.readline().rstrip()

total = 0
T = int(input())
result = ''

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    mx = arr[0]
    mx_start = mx_end = 0

    start = end = 0

    for i in range(1, N):
        if arr[i] >= arr[i-1] + arr[i]:
            start = i
            end = i
        else:
            arr[i] = arr[i-1] + arr[i]
            end = i
            
        if arr[i] > mx:
            mx = arr[i]
            mx_end = end
            mx_start = start
        elif arr[i] == mx and mx_end - mx_start > end - start:
            mx = arr[i]
            mx_end = end
            mx_start = start

    result += f'{mx_start + 1} {mx_end + 1}\n'
    total += mx

print(total)
print(result)

