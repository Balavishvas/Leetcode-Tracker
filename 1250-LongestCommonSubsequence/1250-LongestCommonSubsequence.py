# Last updated: 7/14/2026, 2:15:54 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1,len2=len(text1),len(text2)
        dp=[[None]*len2 for i in range(len1)]

        for i in range(len1):
            if text1[i]==text2[0]:
                dp[i][0]=1
            else:
                if i==0:
                    dp[i][0]=0
                else:
                    dp[i][0] = dp[i-1][0]
        
        for i in range(len2):
            if text1[0]==text2[i]:
                dp[0][i]=1
            else:
                if i==0:
                    dp[0][i]=0
                else:
                    dp[0][i]=dp[0][i-1]
        
        for i in range(1,len1):
            for j in range(1,len2):
                if text1[i]==text2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[len1-1][len2-1]