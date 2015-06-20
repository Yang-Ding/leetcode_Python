class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        x=0
        for i in range(len(nums)):
           x^=nums[i] # python xor operation  
        return x
