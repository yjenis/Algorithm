def solution(s):
    stack=[]
    for i in s:
        if i=="(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
                # if now=="(":
                continue
            else:
                return False
    if stack:
        return False
    else:
        return True