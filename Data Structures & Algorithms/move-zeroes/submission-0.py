class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nzr =0
        zr = -1
        while nzr < len(nums):
            print(nzr)
            print(zr)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            if zr == -1 and nums[nzr] == 0:
                zr = nzr
            elif zr != -1 and nums[nzr] != 0:
                nums[nzr], nums[zr] = nums[zr] ,nums[nzr]
                zr +=1
            nzr +=1