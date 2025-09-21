def solution(n):
    answer = 1
    numbers=[i for i in range(n+1)]
    start,end=1,n
    # print(numbers[start],numbers[n])
    now=0
    for i in range(start,end+1): # 초기 now 값
        now+=i
    print(now)
    
    while start<end:
        # print(start,end)
        if end==start:
                start-=1
                now+=numbers[start]
                end+=1
                now-=numbers[end]
                print("end==start: ",now, start, end)

        elif now==n:
            print("똑같다: ", now,start,end)

            answer+=1
            now-=numbers[start]
            start+=1
            # end-=1
            # now-=numbers[end]
            # print("갱신: ",now, start, end)
            
        if now>n:
            # print("크다: ", now,start,end)
            now-=numbers[end]
            end-=1
        
        elif now<n:
            # print("작다: ", now,start,end)
            # if start
            now-=numbers[start]
            start+=1
            end+=1
            now+=numbers[end]
            
        
    return answer