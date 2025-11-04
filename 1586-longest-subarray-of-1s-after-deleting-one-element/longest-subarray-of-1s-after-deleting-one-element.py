class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        maxlen = 0
        k = 1
        while end < len(nums):
            if nums[end] == 0:
                k -= 1
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
    
            maxlen = max(maxlen, end - start + 1)
            end += 1
        return maxlen - 1


