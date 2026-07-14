# Last updated: 7/14/2026, 2:16:31 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]