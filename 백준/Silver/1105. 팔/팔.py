L, R = map(int, input().split())

# L과 R의 길이가 다르면 8이 없는 숫자가 존재할 수 있으므로 0 출력
if len(str(L)) != len(str(R)):
    print(0)
else:
    L, R = str(L), str(R)
    cnt = 0
    
    # 앞에서부터 같은 숫자가 나오는 동안만 확인
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break  # 달라지는 순간부터는 8의 개수를 더 셀 필요 없음
    
    print(cnt)
