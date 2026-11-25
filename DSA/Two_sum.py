def two_sum(nums,target):
    seen={}
    for index,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [seen[complement],index]
        seen[num]=index
    return None
print(two_sum([1,3,5,4],9))