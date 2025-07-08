class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            # Ensure mid is even (pair starts at even index)
            if mid % 2 == 1:
                mid -= 1
            # Compare pair
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]
            