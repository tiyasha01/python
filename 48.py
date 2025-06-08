#counting number of days in a given month of a year
month=6
year=2026
if(month==2 and year%400==0) or (year%100==0 and year%400==0):
    print("no of days is 28")
elif month==2:
    print("no of days is 29")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("no of days is 31")
else:
    print("no of days is 30")
    