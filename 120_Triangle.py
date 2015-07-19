import copy
from copy import deepcopy
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self,triangle):
        if len(triangle)==1:
            return triangle[0][0]
        m=len(triangle)
        formerL=deepcopy(triangle[0])
        curL=[]
        for i in range(m-1): # how many layers to we need to build up
            for j in range(i+2):
                if j==0:
                    curL.append(formerL[0]+triangle[i+1][0])
                elif j==i+1:
                    curL.append(formerL[-1]+triangle[i+1][-1])
                else:
                    curL.append(min(formerL[j-1],formerL[j])+triangle[i+1][j])
            formerL=deepcopy(curL)
            curL=[]
            #print formerL
        return min(formerL)
