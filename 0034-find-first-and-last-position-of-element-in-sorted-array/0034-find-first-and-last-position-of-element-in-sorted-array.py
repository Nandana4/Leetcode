class Solution(object):
    def searchRange(self, nums, target):
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        first = mid
                    right = mid - 1
            return first

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        last = mid
                    left = mid + 1
            return last

        return [find_first(nums, target), find_last(nums, target)]
