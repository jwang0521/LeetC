class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = max_sum = sum(nums[:k])
        for i in range(len(nums)-k):
            curr_sum += nums[i+k] - nums[i]
            max_sum = max(max_sum, curr_sum)
        return float(max_sum)/k