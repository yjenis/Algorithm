a,b,c=map(int,input().split())

def pow(x,y,z):
    # return (x**y)%z
    if y==1:
        return x%z

    if y%2==0:
        a=pow(x,y/2,z)
        return a*a%z

    else:
        b=pow(x,(y-1)/2,z)
        return b*b*x%z

print(pow(a,b,c))