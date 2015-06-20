from math import pow, log10
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:
            return False
        elif x==0:
            return True
        else:
            N=int(log10(x))+1
            cur=x
            curN=N
            for i in range(N/2):
                left=cur/int(pow(10,curN-1))
                right=cur%10
                cur=(cur-left*int(pow(10,curN-1)))/10
                curN=curN-2
                if left!=right:
                    return False
        return True
