class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new=sorted(nums)
        i=0
        while i<len(nums):
            k=nums.pop(0)
            nums.append(k)
            if nums == new:
                return True
            i=i+1
        return False

