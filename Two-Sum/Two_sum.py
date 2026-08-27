def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                return [i,j]
nums=[]
Number=int(input("Enter how Many numbers you want to store in list: "))
for i in range(Number):
    Num=int(input(f"Enter The {i+1} number: "))
    nums.append(Num)
target=int(input("Enter the Target Number:"))
res=two_sum(nums,target)
print("Result",res)