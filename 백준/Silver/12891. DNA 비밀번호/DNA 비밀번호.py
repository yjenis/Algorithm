s,p=list(map(int,input().split()))
letters=list(input())
stand=list(map(int,input().split()))
first=[0]*4
point=0
cnt=0

def plust(l):
    global point, first, stand
    if letters[l]=="A":
        first[0]+=1
        # if stand[0]<=first[0]:
            # point+=1
    elif letters[l] =='C':
        first[1] += 1
        # if stand[1] <= first[1]:
            # point += 1

    elif letters[l] == 'G':
        first[2] += 1
        # if stand[2] <= first[2]:
            # point += 1
    else:
        first[3] += 1
        # if stand[3] <= first[3]:
            # point += 1

def minus(m):
    global point, first, stand
    if letters[m] == "A":
        first[0] -= 1
        # if stand[0] > first[0]:
            # point -= 1
    elif letters[m] == 'C':
        first[1] -= 1
        # if stand[1] > first[1]:
            # point -= 1

    elif letters[m] == 'G':
        first[2] -= 1
        # if stand[2] > first[2]:
            # point -= 1
    else:
        first[3] -= 1
        # if stand[3] > first[3]:
            # point -= 1



# 첫 번째 부분 문자열 만들기(기준이 됨)
for i in range(p):
    if letters[i]=='A':
        first[0]+=1
        # if stand[0]<=first[0]:
        #     break
        # else:
        #     point += 1
    elif letters[i]=='C':
        first[1]+=1
        # if stand[1]<=first[1]:
        #     break
        # else:
        #     point+=1

    elif letters[i]=='G':
        first[2]+=1
        # if stand[2]<=first[2]:
        #     break
        # else:
        #     point += 1
    else:
        first[3]+=1
        # if stand[3]<=first[3]:
        #     break
        # else:
        #     point += 1
for i in range(4):
    if first[i]>=stand[i]:
        point+=1


if point==4:
    cnt+=1

for i in range(1,s-p+1):
    start,end=i,i+p-1
    minus(start-1)
    plust(end)
    point2=0
    for j in range(4):
        if first[j] >= stand[j]:
            point2 += 1
        else:
            break
    if point2==4:
        cnt+=1

print(cnt)
