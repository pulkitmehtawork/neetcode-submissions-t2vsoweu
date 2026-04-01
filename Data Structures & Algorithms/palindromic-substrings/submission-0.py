class Solution:
    def countSubstrings(self, s: str) -> int:
        palin_sub = set()

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palin_sub.add((s[l:r+1],l+r))
                l -=1
                r +=1

            l =i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palin_sub.add((s[l:r+1], l+r))
                l -=1
                r +=1
        return len(palin_sub)
        