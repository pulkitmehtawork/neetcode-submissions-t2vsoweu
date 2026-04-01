class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3

        for num in nums:
            arr[num] += 1
        print(arr)
        i = 0
        for ind in range(len(arr)):
            while arr[ind] :
                arr[ind] -= 1
                nums[i] = ind
                i += 1
        return nums

