class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=set(nums)
        p=range(1,len(nums)+1)
        miss=[]
        for i in range(len(p)):
            if p[i] not in k:
                miss.append(p[i])
        return miss

        