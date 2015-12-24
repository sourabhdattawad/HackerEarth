import math
n = int(raw_input())
for i in range(n):
    n= int(raw_input())
    n= math.factorial(n)
    a = n
    count=0
    while(n%10==0):
        count+=1
        n=n/10
    print count
