class Solution:
    def reverseArray(self, arr):
        n = len(arr)

        temp = [0] * n

        for i in range(n):
            temp[i] = arr[n - i - 1]

        for i in range(n):
            arr[i] = temp[i]
