# Last updated: 7/22/2026, 12:08:42 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums)==1:
4            return nums[0]
5        dp=[0]*len(nums)
6        dp[0]=nums[0]
7        dp[1]=max(nums[0],nums[1])
8        for i in range(2,len(nums)):
9            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
10        return dp[-1]