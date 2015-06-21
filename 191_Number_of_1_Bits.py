class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        x=n
        s=''
        while(x>0):
            s=str(x%2)+s
            x=x/2
        counter=0
        for i in range(len(s)):
            if s[i]=="1":
                counter+=1
        return counter
