from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)

print(searchInsert(nums = [1,3,5,6], target = 2))