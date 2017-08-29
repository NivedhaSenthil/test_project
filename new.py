i=1
n=int(input("Enter the length of the floyds triangle"))
z=1
k=0
while z in range(n+1):
    for k in range(z):
        print(i,end="")
        i+=1
    k=0
    z+=1
    print("\n")
