import math

n=int(input())

def isPrime(number):
    if number<2:
        return False
    std=int(math.sqrt(number)) #square root
    for i in range(2,std+1):
        if number%i==0:
            return False
    return True


def dfs(a,cnt):
    if cnt==n:
        print(a)
        return

    odds = [1, 3, 5, 7, 9]
    for odd in odds:
        new=a*10+odd
        if isPrime(new):
            dfs(new,cnt+1)

stack=[7,5,3,2]

while stack:
    a=stack.pop()
    dfs(a,1)