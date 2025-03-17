nums=(1,4,9,16,25,36,49,64,81,100)
x=36
index=0
while index<len(nums):
    if(nums[index]==x):
        print("found at index",index)
    else:
        print("finding...")
    index+=1
