def merge(nums1, m, nums2, n):
    merged = sorted(nums1[:m] + nums2[:n])
    for i in range(len(merged)):
        nums1[i] = merged[i]

    return nums1
print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))