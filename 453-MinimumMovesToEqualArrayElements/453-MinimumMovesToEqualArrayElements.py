# Last updated: 7/14/2026, 2:16:09 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum=min(nums)
        count=0
        for num in nums:
            count+= num-minimum
        return count