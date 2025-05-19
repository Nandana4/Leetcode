class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None. Modify nums in-place.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n
        nums[:] = nums[-k:] + nums[:-k]
