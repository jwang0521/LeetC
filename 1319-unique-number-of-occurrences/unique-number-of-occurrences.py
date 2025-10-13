class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        count = Counter(arr)

        occurance = list(count.values())
        return len(occurance) == len(set(occurance))
        


        