import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        for num in nums:
            heapq.heappush_max(self.max_heap, num) 

    def add(self, val: int) -> int:
        heapq.heappush_max(self.max_heap, val)
     
        return heapq.nlargest(self.k, self.max_heap)[-1]