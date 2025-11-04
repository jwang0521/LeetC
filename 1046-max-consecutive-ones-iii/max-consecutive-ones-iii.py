class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxlen = 0
        start = 0
        end = 0
        while end < len(nums):
            if nums[end] == 0:
                k -= 1
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
            end += 1
        return maxlen

            

            
        