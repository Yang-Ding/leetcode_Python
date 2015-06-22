class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        Dic={}
        keys=set()
        L=[]
        for i in range(len(s)-9):
            if s[i:i+10] not in keys:
                Dic[s[i:i+10]]=1
                keys.add(s[i:i+10])
            else:
                Dic[s[i:i+10]]+=1
        for key in keys:
            if Dic[key]>1:
                L.append(key)
        return L
