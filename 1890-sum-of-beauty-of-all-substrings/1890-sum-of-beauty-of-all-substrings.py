class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            freq = [0] * 26  # Frequency array for a-z
            for j in range(i, len(s)):
                char_index = ord(s[j]) - ord('a')
                freq[char_index] += 1

                max_freq = max(freq)
                min_freq = min([f for f in freq if f > 0])  # Only consider non-zero

                total += max_freq - min_freq

        return total
