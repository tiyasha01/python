#quadrant in which coordinate lie
x,y=map(int,list(input("insert value for x and y:").split(" ")))
if x>0 and y>0:
    print("point (",x,",",y,") lies in the first quadrant")
elif x<0 and y>0:
    print("point (",x,",",y,") lies in the second quadrant")
elif x<0 and y<0:
    print("point (",x,",",y,") lies in the third quadrant")
elif x>0 and y<0:
    print("point (",x,",",y,") lies in the fourth quadrant")
elif x==0 and y==0:
    print("point (",x,",",y,") lies in the origin")
elif x!=0 and y==0:
    print("point (",x,",",y,") lies at x-axis")
elif x==0 and y!=0:
     print("point (",x,",",y,") lies at y-axis")