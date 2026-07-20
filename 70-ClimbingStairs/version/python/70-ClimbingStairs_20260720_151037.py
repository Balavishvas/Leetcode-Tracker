# Last updated: 7/20/2026, 3:10:37 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n==1:
4            return 1
5        if n==2:
6            return 2
7        dp=[1]*n
8        dp[1]=2
9        for i in range(2,n):
10            dp[i]=dp[i-1]+dp[i-2]
11        return dp[-1]