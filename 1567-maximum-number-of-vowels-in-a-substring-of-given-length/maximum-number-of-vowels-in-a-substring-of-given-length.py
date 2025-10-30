class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #sliding window
        maxVowels = 0
        left = 0
        vowel = 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                vowel += 1
            if (i-left +1) == k:
                maxVowels = max(maxVowels, vowel)
                if s[left] in "aeiou":
                    vowel -= 1
                left += 1
        return maxVowels
            


        