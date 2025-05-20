class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        extra = []
        c = nums.count(0)
        for j in range(c):
            extra.append(0)
        non_zero = [x for x in nums if x != 0]
        nums[:] = non_zero + extra 