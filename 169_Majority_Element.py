class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        Dic={}
        for item in nums:
            Dic[item]=0
        for item in nums:
            Dic[item]+=1
        for item in Dic.keys():
            if Dic[item]>len(nums)/2:
                return item
        return -1
