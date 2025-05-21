class Solution:
    def subarraySum(self, nums, k):
        sum_freq = {}
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            if current_sum == k:
                result += 1
            target_diff = current_sum - k
            if target_diff in sum_freq:
                result += sum_freq[target_diff]
            sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1

        return result

        