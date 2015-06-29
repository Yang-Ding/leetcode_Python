class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows==1:
            return s
        L=[]
        for i in range(numRows):
            L.append("")
        row=[]
        for i in range(numRows):
            row.append(i)
        for i in range(numRows-2):
            row.append(numRows-i-2)
        for i in range(len(s)):
            index=row[i%(numRows*2-2)]
            L[index]+=s[i]
        output=""
        for item in L:
            output+=item
        return output
