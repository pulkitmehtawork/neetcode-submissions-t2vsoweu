class Solution:
    def isPalindrome(self, x: int) -> bool:
        # get all digits
        if x < 0:
            return False
        digits = []
        while x>0:
            digits.append(x %10)
            x = x // 10

        # two pointer iterate through all digits and check if they r equal
        l = 0
        r = len(digits)-1
        while l < r:
            if digits[l] != digits[r]:
                return False
            l +=1
            r -=1
        return True