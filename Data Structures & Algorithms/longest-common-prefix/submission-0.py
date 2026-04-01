class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ### smallest word

        smallest = 10000000
        smallest_word = ''
        for word in strs:
            if len(word) < smallest:
                smallest = len(word)
                smallest_word = word
        print(smallest_word)
        print(word)
        res = ''
        for i in range(smallest):
            for word in strs:
                if word[i] != smallest_word[i]:
                    return res
            res += smallest_word[i]
        return res
