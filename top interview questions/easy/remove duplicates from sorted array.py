def removeDuplicates(nums: list):
    left = 0
    for right in range(len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]

    return len(nums[:left+1]), nums


print(removeDuplicates([1,1,2,3,4,4]))