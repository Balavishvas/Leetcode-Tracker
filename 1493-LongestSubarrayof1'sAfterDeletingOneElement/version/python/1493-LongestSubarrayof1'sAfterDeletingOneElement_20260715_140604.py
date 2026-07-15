# Last updated: 7/15/2026, 2:06:04 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        l=0
4        r=len(nums)-1
5        
6        while l<r:
7            mid=(l+r)//2
8            if mid%2 ==1:
9                mid-=1
10            if nums[mid]==nums[mid+1]:
11                l=mid+2
12            else:
13                r=mid            
14        return nums[l]
15
16                
17            