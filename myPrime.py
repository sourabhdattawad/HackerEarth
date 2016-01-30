m = int(raw_input())
n = map(eval, raw_input().split())
for i in range(len(n)):
    b = n[:]
    flag=0
    a = b.pop(i)

    for i in b:
        if(a%i==0):
            flag=1
    if(flag==0):
        print a,
        
        
    
