class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1=sorted(nums1)
        print(nums1)
        if len(nums1)%2!=0:
            return nums1[len(nums1)/2]
        else:
            avg = (nums1[(len(nums1) - 1) // 2] + nums1[len(nums1) // 2]) / 2.0
            return avg