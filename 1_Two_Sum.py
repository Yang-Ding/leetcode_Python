ss Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        L=set(nums)
        for i in range(len(nums)):
            remainder=target-nums[i]
            if remainder in L:
                for j in range(i+1,len(nums)):
                    if remainder==nums[j]:
                        return [i+1,j+1]
