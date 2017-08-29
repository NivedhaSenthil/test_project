
import datetime
print("Enter the date")
year=int(input("Enter the year"))
day=int(input("Enter the day"))
m=int(input("Enter the month"))
date1=datetime.date(year,m,day)
print(date1)
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    
    if day<31:
        day1=day+1
    else:
        if day==31:
            day1=1
            if m==12:
                m=1
                year+=1
            else:
                m=+1
        else:
            print("Invalid date")
            exit
else:
    if m==4 or m==6 or m==9 or m==11:
        
        if day<30:
            day1=day+1
        else:
            if day==30:
                day1=1
                m+=1
    else:
        if m==2:
            if year%4==0:
                
                if day<29:
                    day1=day+1
                else:
                    if day==29:
                        day1=1
                        m=m+1
                    else:
                        print("Invaalid date")
            else:
                
                if day<28:
                    day1=day+1
                else:
                    if day==28:
                        day1=1
                        m=m+1
                    else:
                        print("Invaalid date")
date2=datetime.date(year,m,day1)
print(date2)
