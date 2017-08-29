a=[]
b=[]
n1=int(input("Enter the number of element in the list"))
c=[int(input("Enter the elements to be insterted ")) for i in range(1,n1+1)]
n2=int(input("Enter the number of element in the list"))
a=[int(input("Enter the elements to be insterted ")) for i in range(1,n2+1)]
new=a+c
new.sort()
print("The largest element in the list is ")
print (new)
