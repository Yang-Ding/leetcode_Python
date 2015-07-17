class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        curN=n
        while(curN>1):
            if curN%2!=0:
                return False
            curN=curN/2
        if curN==1:
            return True
        else:
            return False
