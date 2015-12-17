from fractions import gcd
n = int(raw_input())
for _ in range(n):
    k=int(raw_input())
    count=0
    for i in range(1,k+1):
        if(gcd(i,k)==1):
            count+=1
    print count
