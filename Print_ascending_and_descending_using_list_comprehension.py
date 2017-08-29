a=[]
i=1
n=int(input("Enter the number of element in the list"))
a=[int(input("Enter the elements to be insterted ")) for i in range(1,n+1)]
print (sorted(a,key=int,reverse=True))
a.sort()
print("The largest element in the list is ")
print (a)
