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
        for right in range(len(s)):
            if s[right] in "aeiou":
                vowel += 1
            if (right-left +1) == k:
                maxVowels = max(maxVowels, vowel)
                if s[left] in "aeiou":
                    vowel -= 1
                left += 1
        return maxVowels
            


        