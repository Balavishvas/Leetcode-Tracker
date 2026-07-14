# Last updated: 7/14/2026, 2:16:58 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=nums[0]
        c=0

        for i in nums:
            if c<0:
                c=0
            c+=i
            if c>m:
                m=c
        return m

        