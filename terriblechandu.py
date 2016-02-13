tc = int(raw_input())
for _ in range(tc):
    string = list(raw_input())
    newstr = string[::-1]
    result =""
    for i in newstr:
        result+=i
    print result
