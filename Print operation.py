n=int(input())
i=0
a=[]
for i in range(0,n+1):
    z=input().strip().split(" ")
    i+=1
    if z[0]=="insert":
        a.insert(int(z[1]),int(z[2]))
    elif z[0]=="remove":
        a.remove(int(z[1]))
    elif z[0]=="append":        
        a.append(int(z[1]))
    elif z[0]=="pop":
        a.pop()
    elif z[0]=="sort":
        a.sort()
    elif z[0]=="reverse":
        a.reverse()
    elif z[0]=="print":
        print(a)
    else:
        print("Invalid statement")
