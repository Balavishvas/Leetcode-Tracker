# Last updated: 7/14/2026, 2:17:13 PM
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={ "(":")","[":"]","{":"}" }

        for i in s:
            if i in d.keys():
                st.append(i)
            else:
                if st==[]:
                    return False
                else:
                    if d[st[-1]]==i:
                        st.pop()
                    else:
                        return False
        
        if st==[]:
            return True
        else:
            return False
