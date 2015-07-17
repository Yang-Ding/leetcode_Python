import sys
sys.setrecursionlimit(1000000)
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def Merge(self,L1,L2):
        counter1=0
        counter2=0
        L=[]
        while(counter1<len(L1) and counter2<len(L2)):
            if L1[-1]<=L2[0]:
                return L1+L2
            else:
                if L1[counter1]<=L2[counter2]:
                    L.append(L1[counter1])
                    counter1+=1
                else:
                    L.append(L2[counter2])
                    counter2+=1
        if counter1<len(L1):
            return L+L1[counter1:]
        elif counter2<len(L2):
            return L+L2[counter2:]
        return L
            
        
    def MergeSort(self,nums):
        if len(nums)==1:
            return nums
        middle=len(nums)/2
        left=nums[:middle]
        right=nums[middle:]
        sorted_left=self.MergeSort(left)
        sorted_right=self.MergeSort(right)
        L=self.Merge(sorted_left,sorted_right)
        return L
        
    def findKthLargest(self, nums, k):
        L=self.MergeSort(nums)
        return L[-k]
