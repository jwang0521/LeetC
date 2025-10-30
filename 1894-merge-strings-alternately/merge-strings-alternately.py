class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        l1 = len(word1)
        l2 = len(word2)
        merged = ""

        while i < l1 and j < l2:
            merged += word1[i] + word2[j]
            i += 1
            j += 1
        if i < l1:
            merged += word1[i:]
        else:
            merged += word2[j:]
            
        return merged