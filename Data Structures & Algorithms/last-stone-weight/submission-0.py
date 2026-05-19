import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for weight in stones:
            heapq.heappush_max(max_heap, weight)

        while len(max_heap) > 1:
            heaviest = heapq.heappop_max(max_heap)
            second_heaviest = heapq.heappop_max(max_heap)

            if heaviest == second_heaviest:
                continue
            elif heaviest < second_heaviest:
                heapq.heappush_max(max_heap, second_heaviest - heaviest)
            else:
                heapq.heappush_max(max_heap, heaviest - second_heaviest)

        if not max_heap:
            return 0
        return heapq.heappop_max(max_heap)
        