def solution(s):

    answer = []
#     spl=s.split('}'
    s = s[2:-2].split('},{')
    s = [w.split(',') for w in s]
    s.sort(key=len)
    # print(s)
    for a in s:
        for w in a:
            if int(w) not in answer:
                answer.append(int(w))
    return answer
