def missing_number(nums):
    missing=len(nums)
    for index,num in enumerate(nums):
        missing^=index^num
    return missing

print(missing_number([1,0,3]))