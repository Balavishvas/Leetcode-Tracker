# Last updated: 7/14/2026, 2:15:53 PM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]

        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if nums[i]> nums[j]:
                    count+=1
            ans.append(count)
        return (ans)