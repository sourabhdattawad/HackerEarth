n = int(raw_input())
lst = map(int, raw_input().split())
m = int(raw_input())
while(m):
    k = int(raw_input())
    for i in range(len(lst)):
        lst[i]=int(lst[i]/k)
    m-=1
for i in lst:
	print i,
