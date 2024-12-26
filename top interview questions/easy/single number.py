from typing import List

def singleNumber(nums: List[int]) -> int:
    occurance = {}

    for number in nums:
        if number in occurance:
            occurance[number] += 1
        else:
            occurance[number] = 1

    for num, count in occurance.items():
        if count == 1:
            return num
    return