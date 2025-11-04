from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False
            
        count1 = sorted(Counter(word1).values())
        count2 = sorted(Counter(word2).values())
        if count1 != count2:
            return False
        
        return True
        