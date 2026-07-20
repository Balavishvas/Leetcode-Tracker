# Last updated: 7/20/2026, 3:11:41 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n==1:
4            return 1
5        dp=[1]*n
6        dp[1]=2
7        for i in range(2,n):
8            dp[i]=dp[i-1]+dp[i-2]
9        return dp[-1]