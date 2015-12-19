from itertools import chain, combinations
 
def powerset(iterable):
  xs = list(iterable)
  return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )

tc = int(raw_input())
for i in range(tc):
    ele= int(raw_input())
    arr= map(int, raw_input().split())
    num = int(raw_input())
    comb = list(powerset(arr))
    flag=0
    for i in range(len(comb)):
        if(sum(comb[i])==num):
            flag=1
            break
    if(flag==1):
        print "YES"
    else:
        print "NO"
