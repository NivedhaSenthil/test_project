k=["manikumar","kase","bhake","dhanapal","dinesh","Thulir","pravasthi"]
b=input("Enter the start letter to search")
s=input("Enter the End letter to search")
i=0
for i in range(0,len(k)):
    if b in k[i][0]:
        print(k[i])
    if s in k[i][-1]:
        print(k[i])
    i+=1
