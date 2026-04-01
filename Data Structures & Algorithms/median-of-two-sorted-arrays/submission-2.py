class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. make shorter array as A , longer as B


        A, B = nums1 , nums2

        if len(nums2) < len(nums1):
            A , B = B , A

        


        # go for binary search in shorter array
        l=0
        r = len(A) -1
        half = (len(A) + len(B)) // 2
        while True:
            i = (l + r) // 2
            j = half - i -2 


            Aleft = A[i] if i >=0 else -float('inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')


            Bleft = B[j] if j >=0 else -float('inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            if Aleft <=Bright and Aright >= Bleft:
                if (len(A) + len(B)) % 2:
                    return min(Aright, Bright)
                return (min(Aright, Bright) + max(Aleft , Bleft)) / 2
            elif Aleft > Bright:
                r = i -1
            else:
                l = i+1






        # out of bound case
        ### odd , even case






