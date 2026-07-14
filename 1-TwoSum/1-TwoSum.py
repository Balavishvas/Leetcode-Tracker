# Last updated: 7/14/2026, 2:17:21 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            value=nums[i]
            difference = target-value
            if value not in d:
                d[difference]=i
            else:
                current_index = i
                previous_index =d[value]
                return [current_index,previous_index]