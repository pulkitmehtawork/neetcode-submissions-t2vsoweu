class Solution:
    def firstUniqChar(self, s: str) -> int:
        chr_hash = {}
        for c in s:
            chr_hash[c] = 0 

        for c in s:
            chr_hash[c] +=1

        for i,c in enumerate(s):
            if chr_hash[c] == 1:
                return i
        return -1

        

        