class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        s=s.upper()
        if len(s)==0:
            return True
        while(left<right):
            if s[left].isalnum()==False:
                left+=1
                continue
            if s[right].isalnum()==False:
                right-=1
                continue
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
