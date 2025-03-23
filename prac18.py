#recursive function to calculate sum of n natural numbers
def calc(n):
    if(n==0):
        return 0
    return calc(n-1)+n
print (calc(5))