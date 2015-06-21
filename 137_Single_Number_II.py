class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        Dic={}
        for item in set(nums):
            Dic[item]=0
        for item in nums:
            Dic[item]+=1
        for key in Dic.keys():
            if Dic[key]!=3:
                return key
