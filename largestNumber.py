def find_largest(nums):
    if not nums: 
        return None
    largest = nums[0] 
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 5, 7, 2, 8]))  
print(find_largest([]))               
