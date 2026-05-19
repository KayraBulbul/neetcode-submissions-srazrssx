import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for num in nums:
            heapq.heappush_max(max_heap, num)

        return heapq.nlargest(k, max_heap)[-1]