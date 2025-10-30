class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] == k:
                ans += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
                
        return ans