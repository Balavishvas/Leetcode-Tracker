# Last updated: 7/14/2026, 2:15:56 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        