import heapq
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # add everything into maxheap-- smaller
        heapq.heappush(self.small , -1*num)
        # check if max in small heap is larger then min heap of larger
        if self.small and self.large and -1 *self.small[0] > self.large[0]:
            val =-1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        


        # check size diff
        if len(self.small) > len(self.large) +1 :
            val =-1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small) +1 :
            val =heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
        





    def findMedian(self) -> float:
        
        # check if size diff
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (self.large[0] + -1*self.small[0]) / 2

        # else equal


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()