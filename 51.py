#finding roots of a quadratic equation
import math
def findRoots(a,b,c):
    if a==0:
        print("invalid")
        return -1
    d=b*b-4*a*c
    sqrt_val=math.sqrt(abs(d))
    if d>0:
        print("roots are real and different")
        print((-b+sqrt_val)/(2*a))
        print((-b-sqrt_val)/(2*a))
    elif d==0:
        print("roots are real and same")
        print(-b/(2*a))
    else:
        print("roots are complex")
        print(-b/(2*a),"+i",sqrt_val)
        print(-b/(2*a),"-i",sqrt_val)
a=1
b=4
c=4
findRoots(a,b,c)