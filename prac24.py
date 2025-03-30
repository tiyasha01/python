#from a file containing numbers separated by comma,print the count of even numbers
c=0
with open("practice.txt","r") as f:
    data=f.read()
    num=data.split(",")
    for val in num:
        if(int(val)%2==0):
            c+=1
print(c)
