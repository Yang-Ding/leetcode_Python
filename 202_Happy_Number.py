from math import pow
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, newN):
        cycle=0
        curN=newN
        L=set()
        s=0
        while(s!=1):
            s=0
            while(curN>0):
                s+=pow(curN%10,2)
                curN=curN/10
            curN=int(s)
            if int(s) in L:
                return False
            else:
                L.add(int(s))
            if int(s)==1:
                    return True
        return False
