import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        for num in nums:
            heapq.heappush_max(self.max_heap, num) 

    def add(self, val: int) -> int:
        num = 0
        k_copy = self.k
        heapq.heappush_max(self.max_heap, val)
     
        return heapq.nlargest(self.k, self.max_heap)[-1]