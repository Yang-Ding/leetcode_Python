class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        Dic={}
        keys=set()
        for i in range(len(nums)):
            if nums[i] not in keys:
                keys.add(nums[i])
            else:
                if i-Dic[nums[i]]<=k:
                    return True
            Dic[nums[i]]=i
        return False
