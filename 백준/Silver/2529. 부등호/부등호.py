k = int(input())
sign = list(map(str, input().split()))
visitied = [False] * 11
minResult = ""
maxResult = ""


def possible(i, j, sign):
    if sign == '>':
        return i > j
    else:
        return i < j


def solve(depth, s):
    global minResult, maxResult

    if depth == k + 1:
        if len(minResult) == 0:
            minResult = s
        else:
            maxResult = s
        return

    for i in range(10):
        #i에 방문하지 않았다면
        if not visitied[i]:
            #문자열이 아직 존재하지 않거나, 계산이 가능한 경우
            if depth == 0 or possible(s[len(s) - 1], str(i), sign[depth - 1]):
                visitied[i] = True
                #문자열 1개 추가
                solve(depth + 1, s + str(i))
                #방문 표시 제거
                visitied[i] = False


solve(0, "")
print(maxResult)
print(minResult)
