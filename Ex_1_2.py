import random as rd
a=list(map(int,input().split()))
n=int(input())
def random(n):
    l=rd.randint(0,n-1)
    return l
result=random(n)
def check(a,result):
    for i in range(len(a)):
        if a[i] != result:
            pass
        else:
            return True
check(a,result)
while check(a,result) == True:
    check(a,result)
    result=random(n)
    print("load...")
print(result)