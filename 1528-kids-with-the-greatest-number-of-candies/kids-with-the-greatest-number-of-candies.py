class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        result = []
        max_candies = max(candies)
        for each in candies:
            if each + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result

        
        