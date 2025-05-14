class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in nums:
            x=i*i
            new.append(x)
        new=sorted(new)
        return new