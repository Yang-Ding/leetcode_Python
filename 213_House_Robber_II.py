class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob1(self,nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        s=[0]*len(nums)
        s[0]=nums[0]
        s[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            s[i]=max(s[i-1],s[i-2]+nums[i])
        return s[-1]
    
    def rob(self, nums):
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        else:  
            return max(self.rob1(nums[1:]),self.rob1(nums[:-1]))
