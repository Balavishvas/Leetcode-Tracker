# Last updated: 7/14/2026, 2:16:41 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}

        for i in nums:
            if i not in d:
                d[i]=1
            else:
                if d[i]==1:
                    d[i]+=1
                elif d[i]==2:
                    del d[i]
        return list(d.keys())[0]