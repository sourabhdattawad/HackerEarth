t = int(raw_input())
a = [1000,500,100,50,20,10,5,2,1]    

while(t):
    t-=1
    n = int(raw_input())
    count=0
    while(n!=0):
        for i in a:
            if(i<=n):
                n = n -i            
                count+=1
                
                break
            
    print count
