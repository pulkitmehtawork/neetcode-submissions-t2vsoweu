import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 *heapq.heappop(stones)
            second = -1 *heapq.heappop(stones)

            if first == second:
                continue
            else:
                diff = first - second
                heapq.heappush( stones , -1 * diff,)



        return -1 *heapq.heappop(stones) if stones else 0





        