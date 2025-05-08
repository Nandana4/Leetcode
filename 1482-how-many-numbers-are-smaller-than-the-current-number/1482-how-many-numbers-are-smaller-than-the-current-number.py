class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        k=sorted(nums)
        for i in nums:
            result.append(k.index(i))
        return result 

        