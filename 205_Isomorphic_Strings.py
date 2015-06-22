class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        Dic={}
        for i in range(len(s)):
            if s[i] not in Dic.keys():
                Dic[s[i]]=t[i]
            else:
                if Dic[s[i]]!=t[i]:
                    return False
            if len(Dic.values())!=len(set(Dic.values())):
                return False
        return True
