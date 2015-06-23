from math import sqrt
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):  # Eratosthenes Sieve
        L=[]
        if n<=2:
            return 0
        L=[0,0]+[1]*(n-2)
        for i in range(2,int(sqrt(n-1))+1): # test all the factors
            if L[i]==1:
                factors=range(i**2,n,i)
                for j in factors:
                    L[j]=0
        return sum(L)
