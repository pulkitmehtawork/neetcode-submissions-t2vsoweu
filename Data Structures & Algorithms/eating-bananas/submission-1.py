class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 #min(piles)
        r = max(piles)
        min_k = r
        def is_speed_suff(piles,k,h):
            ans =0
            for p in piles:
                ans += math.ceil(p/k)
            if ans <= h:
                return True
            else:
                return False
        while l <= r:
            mid = (l + r) // 2

            if is_speed_suff(piles , mid , h):
                r = mid -1
                min_k = min(min_k,mid)
            else:
                l = mid +1
            
        return min_k


        