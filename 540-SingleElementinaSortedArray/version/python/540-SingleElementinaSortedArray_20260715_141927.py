# Last updated: 7/15/2026, 2:19:27 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        l=0
4        r=len(nums)-1
5
6        while l<r:
7            mid=(l+r)//2
8
9            if mid%2==1:
10                mid-=1
11            
12            if nums[mid]==nums[mid+1]:
13                l=mid+2
14            else:
15                r=mid
16        return nums[l]
17                
18            