# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

n = int(raw_input())
a=[]
for i in range(n):
    k= map(int, raw_input().split())
    if(k[0]==1):
        if(len(a)==0):
            print "No Food"
        else:
            print a.pop()
    if(k[0]==2):
        a.append(k[1])
        
    
            
    
    

# <codecell>

a=[]
len(a)==0

# <codecell>


