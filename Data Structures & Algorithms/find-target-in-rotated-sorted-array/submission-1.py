class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= nums[0] and target < nums[0]:
                # we are in left sorted array , target is in right
                l = m+1
            elif nums[m] < nums[0] and target >= nums[0]:
                # we r in right , target is in left
                r = m -1
            elif target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m -1
            else:
                return m
        return -1
            

        