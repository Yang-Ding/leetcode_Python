class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if len(s.strip())==0:
            return 0
        else:
            pointer=0
            last_but_two_word=""
            last_word=""
            while(pointer!=len(s)):
                if s[pointer]==" ":
                    if len(last_word.strip())>0:
                        last_but_two_word=last_word
                        last_word=""
                else:
                    last_word+=s[pointer]
                pointer+=1
            if len(last_word.strip())>0:
                return len(last_word)
            else:
                return len(last_but_two_word)
