# Last updated: 7/23/2026, 10:28:37 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        left=0
4        right=0
5        minimum=[]
6        subsum=0
7        while right<len(nums):
8            subsum+=nums[right]
9            while subsum>=target:
10                minimum.append(right-left+1)
11                subsum-=nums[left]
12                left+=1
13            right+=1
14        if len(minimum)==0:
15            return 0
16        else:
17            return min(minimum)