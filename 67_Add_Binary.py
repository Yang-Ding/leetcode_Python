class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        s=""
        extra=0
        a=a.zfill(max(len(a),len(b)))
        b=b.zfill(max(len(a),len(b)))
        for i in range(1,max(len(a),len(b))+1):
            sum=int(a[-i])+int(b[-i])+extra
            s=str(sum%2)+s
            extra=sum/2
        if extra==1:
            s="1"+s
        return s
