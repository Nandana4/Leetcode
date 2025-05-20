class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=[]
        if 1 in nums:
            t.append(1)
        else:
            t.append(0)
        c=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]==1:
                c+=1
                t.append(c)
            else:
                c=1
        return max(t)