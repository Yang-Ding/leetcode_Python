class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums)==0:
            return nums
        elif len(nums)==1:
            return [str(nums[0])]
        else:
            L=[]
            start=nums[0]
            for i in range(len(nums)-1):
                if nums[i]!=nums[i+1]-1 and nums[i]!=nums[i+1]:
                    if start==nums[i]:
                        start=nums[i+1]
                        L.append(str(nums[i]))
                    else:
                        string= str(start) +"->"+ str(nums[i])
                        start=nums[i+1]
                        L.append(string)
            if start==nums[-1]:
                L.append(str(nums[-1]))
            else:
                L.append(str(start)+"->"+str(nums[-1]))
            return L
