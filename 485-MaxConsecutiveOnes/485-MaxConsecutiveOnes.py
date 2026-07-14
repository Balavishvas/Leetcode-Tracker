# Last updated: 7/14/2026, 2:16:08 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=[]
        maxOnes=0
        for i in nums:
            if i==0:
                ans.append(maxOnes)
                maxOnes=0
            else:
                maxOnes += 1
        ans.append(maxOnes)
        return max(ans)
