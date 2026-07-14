# Last updated: 7/15/2026, 1:37:47 AM
1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3        zero=0
4        
5        max_count=0
6
7        start=0
8        end=0
9
10        while end<len(nums):
11            if nums[end]==0:
12                zero+=1
13            while zero>1:
14                if nums[start]==0:
15                    zero-=1
16                start+=1
17            count=end-start
18            max_count=max(max_count,count)
19            end+=1
20        return max_count
21        