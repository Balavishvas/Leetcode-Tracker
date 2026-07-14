# Last updated: 7/14/2026, 2:16:22 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final=[1]*len(nums)
        prefix=1

        for i in range(len(nums)):
            final[i]=prefix
            prefix=nums[i]*prefix
        
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            final[i]=final[i]*suffix
            suffix=nums[i]*suffix

        return final
        