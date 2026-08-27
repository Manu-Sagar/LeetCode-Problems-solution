def two_sum_V_2(nums,target):
    for i in range(len(nums)):
        need=target-nums[i]
        if(need in nums and nums.index(need)!=i):
            return [i,nums.index(need)]
    print("Target Not Found")


nums=[]
for i in range(int(input("Enter The Number of Elements:"))):
    num=int(input(f"Enter The {i+1} Number:"))
    nums.append(num)
target=int(input("Enter the target Number:"))
res=two_sum_V_2(nums,target)
print("Result:",res)