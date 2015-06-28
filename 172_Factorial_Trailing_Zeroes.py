class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n): # count how many 5
        sum=0
        if n<5:
            return 0
        else:
            sum+=n/5
            sum+=self.trailingZeroes(n/5)
        return sum
