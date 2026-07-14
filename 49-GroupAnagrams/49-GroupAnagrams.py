# Last updated: 7/14/2026, 2:16:59 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        for i in strs:
            s="".join(sorted(i))
            if s not in d:
                d[s]=[i]
            else:
                d[s].append(i)
        return list(d.values())