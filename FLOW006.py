
#sum of digits
T=int(input())
for i in range(T):
    sum=0
    N=int(input())
    for dig in str(N):
        sum=sum+int(dig)
    print(sum)