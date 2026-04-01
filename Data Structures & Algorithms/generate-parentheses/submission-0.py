class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(open_n , close_n):
            if open_n == n and close_n == n:
                res.append("".join(stack))
                return 

            if open_n < n:
                stack.append("(")
                backtracking(open_n + 1 , close_n)
                stack.pop()

            if close_n < open_n:
                stack.append(")")
                backtracking(open_n  , close_n + 1)
                stack.pop()
        backtracking(0,0)
        return res



        