a,b,c=map(int,input().split())
if a+b>c and c+b>a and a+c>b:
    if (a==b and b != c) or (c==b and b != a) or (a==c and b != b):
        print("равнобедренный")
    elif a != b and b != c and c != a:
        print("разностороний")
    else:
        print("равностороний")
else:
    print("не существует")