class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            check=target - nums[i]
            if check in nums and nums.index(check)!=i:
                result.append(i)
                result.append(nums.index(check))
                return result
        return result
        