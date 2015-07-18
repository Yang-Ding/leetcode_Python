class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        L=[1]
        L=L+[0]*len(s)
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and L[j]==1:
                    L[i]=1
        if L[-1]==0:
            return False
        else:
            return True
