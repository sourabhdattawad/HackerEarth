upper = [i for i in range(65,91)]
lower = [i for i in range(97,123)]
tc = int(raw_input())
while(tc):
    tc-=1
    cu=0
    cl=0
    string = raw_input()

    for i in string:
        a = ord(i)
        if(a in upper):
            cu+=1
        elif(a in lower):
            cl+=1
    
    if(cl==0 and cu==0):
        print "Invalid Input"
    else:
        print(min(cu,cl))
        
            
    

    
    
