ss = [1, 1, 1]
def make(x):
    global ss
    if x<=3:
        return ss[-1]
    # for i in range(x):
    new=ss[-2]+ss[-3]
    ss.append(new)
    return make(x-1)

T=int(input())
for _ in range(T):
    ss=[1,1,1]
    N=int(input())
    print(make(N))