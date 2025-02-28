# 두 문자열을 입력받습니다.
str1 = input().strip()
str2 = input().strip()

# dp 테이블을 초기화합니다. dp[i][j]는 str1의 첫 i개 문자와 str2의 첫 j개 문자의 LCS 길이를 저장합니다.
dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

# dp 테이블 채우기
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:  # 두 문자가 같다면
            dp[i][j] = dp[i-1][j-1] + 1
        else:  # 두 문자가 다르면
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# LCS의 길이는 dp[len(str1)][len(str2)]에 저장됩니다.
lcs_length = dp[len(str1)][len(str2)]

# LCS 길이 출력
print(lcs_length)

# LCS 문자열 복원하기
lcs = []
i, j = len(str1), len(str2)

# dp 테이블을 뒤에서부터 거꾸로 따라가며 LCS를 복원합니다.
while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:  # 두 문자가 같다면
        lcs.append(str1[i-1])  # 그 문자를 LCS에 추가
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:  # 위에서 나온 값이 더 크다면
        i -= 1
    else:
        j -= 1

# LCS 문자열은 뒤에서부터 구해졌으므로, 이를 뒤집어서 출력합니다.
print(''.join(reversed(lcs)))
