class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        maxsum=[0]*len(nums)
        maxsum[0]=nums[0]
        for i in range(1,len(nums)):
            maxsum[i]=max(maxsum[i-1]+nums[i],nums[i])
        return max(maxsum)
