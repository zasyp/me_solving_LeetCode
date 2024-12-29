
def pushZerosToEnd(self, nums):
    n = len(nums)
    temp = [0] * n

    j = 0

    for i in range(n):
        if nums[i] != 0:
            temp[j] = nums[i]
            j += 1

    while j < n:
        temp[j] = 0
        j += 1

    for i in range(n):
        nums[i] = temp[i]

