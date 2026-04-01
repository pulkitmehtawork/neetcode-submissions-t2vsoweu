class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        
        res = init
        for i in range(iterations):
            res -= learning_rate * 2 * res
        return round(res,5)
    