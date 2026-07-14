# Last updated: 7/14/2026, 2:15:42 PM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count=0
        
        for s in sentences:
            count=len(s.split())
            if count>max_count:
                max_count=count
        return max_count