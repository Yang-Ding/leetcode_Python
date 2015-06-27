class Solution:
    def numDecodings(self,s):
        if len(s)==0 or s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        NumWays=[0]*(len(s)+1)
        NumWays[1]=1
        if int(s[:2])<=26 and int(s[:2])%10!=0:
            NumWays[2]=2
        elif int(s[:2])>26 and s[1]=='0':
            return 0
        else:
            NumWays[2]=1
        for i in range(2,len(s)):
            if int(s[i-1:i+1])<=26 and s[i-1]!="0" and s[i]!="0":
                NumWays[i+1]=NumWays[i-1]+NumWays[i]
            elif s[i-1]=="0" and s[i]=="0":
                return 0
            elif s[i]=="0" and int(s[i-1:i+1])>26:
                return 0
            elif s[i]=="0":
                NumWays[i+1]=NumWays[i-1]
            else:
                NumWays[i+1]=NumWays[i]
        return NumWays[-1]
