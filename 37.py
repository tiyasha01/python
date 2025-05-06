#permutations in which n people can occupy r seats in a classroom

#function for factorial
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
#user input
n=int(input("enter number of people:"))
r=int(input("enter number of seats:"))
#formula of permutation
p=factorial(n)//factorial(n-r)
print("total possible arrangements are:",p)