# Last updated: 7/14/2026, 2:17:03 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range (len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)