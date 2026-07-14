# Last updated: 7/14/2026, 2:16:32 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        minimum=[]
        subsum=0

        while right<len(nums):
            subsum+=nums[right]
            while subsum>=target:
                minimum.append(right-left+1)
                subsum-=nums[left]
                left+=1
            right+=1
        
        return 0 if len(minimum)==0 else min(minimum)