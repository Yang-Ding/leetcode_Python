class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        minL=[0]*len(nums) # minL[i]: the minimum product ending with nums[i]
        maxL=[0]*len(nums) # maxL[i]: the maximum product ending with nums[i]
        minL[0]=nums[0]
        maxL[0]=nums[0]
        for i in range(1,len(nums)):
            maxL[i]=max(nums[i],maxL[i-1]*nums[i],minL[i-1]*nums[i])
            minL[i]=min(nums[i],maxL[i-1]*nums[i],minL[i-1]*nums[i])
        return max(maxL)
