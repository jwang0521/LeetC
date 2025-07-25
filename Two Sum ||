class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while True:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]
