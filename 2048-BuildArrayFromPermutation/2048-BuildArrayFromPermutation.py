# Last updated: 7/14/2026, 2:15:47 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums)):
            ans.append(nums[nums[i]])
            
        return ans
        