import math
m = int(raw_input())
n = math.factorial(m)
count = 0
while(n%10==0):
    count+=1
    n=n/10
print count
