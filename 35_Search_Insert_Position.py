class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if nums[0]>=target:
            return 0
        if nums[-1]<target:
            return (len(nums))
        for i in range(len(nums)-1):
            if nums[i+1]>=target and nums[i]<target:
                return i+1
