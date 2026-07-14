# Last updated: 7/14/2026, 2:16:49 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        d=[[]]

        for num in nums:
            temp=[]
            for subset in d:
                new_subset=subset+[num]
                temp.append(new_subset)
            d+=temp
        return d 