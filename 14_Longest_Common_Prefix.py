import sys
from sys import maxint
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        else:
            s=""
            minl=maxint
            for item in strs:
                if len(item)<minl:
                    minl=len(item)
            if strs[0]=="":
                return ""
            for i in range(minl):
                consensus=strs[0][i]
                for item in strs:
                    if item[i]!=consensus:
                        return s
                s+=consensus
            return s
