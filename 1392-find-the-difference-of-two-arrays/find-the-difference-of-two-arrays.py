class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        ans 
        """
        set1 = set(nums1)
        set2 = set(nums2)

        list1 = list(set1-set2)
        list2 = list(set2-set1)
        
        return [list1, list2]
                

        