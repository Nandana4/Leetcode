class Solution(object):
    def reversePairs(self, nums):
        def merge_sort(start, end):
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid, end)
            j = mid
            for i in range(start, mid):
                while j < end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid
            # Merge step
            nums[start:end] = sorted(nums[start:end])
            return count

        return merge_sort(0, len(nums))
