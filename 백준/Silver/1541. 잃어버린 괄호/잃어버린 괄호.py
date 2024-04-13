tlr=input().split("-")

numbers=[]
for i in tlr:
    sum=0
    tmp=i.split('+') #덧셈이 붙어있는 수들은 따로 쪼개서 더해서 넣기
    for j in tmp:
        sum+=int(j) #sum에 덧셈해서 집어 넣
    numbers.append(sum)

n=numbers[0]
for i in range(1,len(numbers)):
    n-=numbers[i]
print(n)
