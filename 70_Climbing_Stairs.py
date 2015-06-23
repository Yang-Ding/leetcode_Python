class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n==1:
            return 1
        number_ways=[0]*(n+1)
        number_ways[1]=1
        number_ways[2]=2
        for i in range(3,n+1):
            number_ways[i]=number_ways[i-1]+number_ways[i-2]
        return number_ways[n]
