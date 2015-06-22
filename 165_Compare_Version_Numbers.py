class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        tmp1=version1.split(".")
        tmp2=version2.split(".")
        d=min(len(tmp1),len(tmp2))
        for i in range(d):
            if int(tmp1[i])>int(tmp2[i]):
                return 1
            elif int(tmp1[i])<int(tmp2[i]):
                return -1
        if len(tmp1)>len(tmp2):
            for item in tmp1[len(tmp2):]:
                if int(item)>0:
                    return 1
        elif len(tmp1)<len(tmp2):
            for item in tmp2[len(tmp1):]:
                if int(item)>0:
                    return -1
        return 0
