n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    a=a%10
    if a == 0:
        print(10)  # 0의 거듭제곱은 10번 컴퓨터로 처리됨
        continue

    cycle=[]
    value=a
    
    while value not in cycle:
        cycle.append(value)
        value = (value * a) % 10
    # print(cycle)
    # print((b-1)%len(cycle))
    print(cycle[(b-1)%len(cycle)])
