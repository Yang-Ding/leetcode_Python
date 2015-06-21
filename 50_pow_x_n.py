class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def pow(self,x,n): # non-negative n
        if n%2==0:
            return pow(x,n/2)*pow(x,n/2)
        else:
            return x*pow(x,n/2)*pow(x,n/2)
        
    def myPow(self, x, n):
        if n>=0:
            return pow(x,abs(n))
        else:
            return 1/pow(x,abs(n))
