T=int(input())
for i in range(T):
    fact=1
    n=int(input())
    for diggi in range(1,int(n)+1):
        fact=diggi*fact
    print(fact)
    