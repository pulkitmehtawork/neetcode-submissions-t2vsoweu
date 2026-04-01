class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #num1_num_to_index

        num1_index_map = {}
        num1_index_map = {num:i for i, num in enumerate(nums1)}

        res = [-1] * len(nums1)

        stack = []

        for num in nums2:
            
            while stack and num > stack[-1]:
                val = stack[-1]
                idx = num1_index_map[stack[-1]]
                res[idx] = num
                stack.pop()
            if num in num1_index_map:
                stack.append(num)
        return res