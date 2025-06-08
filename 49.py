#finding no of times x digit occurs in a given input
n= input("Enter the number: ")
x = input("Enter the digit to count: ")
count = 0
for digit in n:
    if digit == x:
        count += 1
print(f"The digit {x} occurs {count} times.")

#another way
def countoccurances(n,d):
    count=0
    while(n>0):
        if(n%10==d):
            count+=1
        n//=10
    return count
d=2
n=122234
print(countoccurances(n,d))