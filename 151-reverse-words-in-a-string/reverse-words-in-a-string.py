class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s.split(" ")

        for i in range(len(s)):
            if s[i]==" ":
                s.pop(i)
            else:
                s[i] = s[i].strip()
                
        s = [x for x in s if x != ""]
        
        rev = s[::-1]
        return " ".join(rev)
        