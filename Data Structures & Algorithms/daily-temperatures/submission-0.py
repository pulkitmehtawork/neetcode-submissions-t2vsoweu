class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for ind , t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append((t , ind))
        return res


        