class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid=len(nums)//2
        start=0
        end=len(nums)-1
        nums.sort()
        while (start<=end):
            if (target<nums[mid]):
                end=mid-1
                mid=(end+start)//2
            elif(target>nums[mid]):
                start=mid+1
                mid=(end+start)//2
            else:
                return mid
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)