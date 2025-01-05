def majorityElement(nums: list) -> int:
    counters = {}
    for i in nums:
        if i in counters:
            counters[i] += 1
        else:
            counters[i] = 1

    for num, count in counters.items():
        if count > len(nums) // 2:
            return num



