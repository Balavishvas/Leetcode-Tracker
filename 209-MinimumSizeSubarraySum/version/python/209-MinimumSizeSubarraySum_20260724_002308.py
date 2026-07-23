# Last updated: 7/24/2026, 12:23:08 AM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix=0
4        count=0
5        mp={0:1}
6
7        for x in nums:
8            prefix+=x
9            if prefix-k in mp:
10                count+=mp[prefix-k]
11            mp[prefix]=mp.get(prefix,0)+1
12        return count