a = int(input("Введите число: "))
k = 0
def pr(a,k):
    for i in range(1, a):
        if (a % i == 0):
            k = k+1
    if (k <= 1):
        return True
    else:
        return False
d=[]

for i in range(1,a):
    if a%i==0 and pr(i,k):
        d.append(i)
print(*d)

