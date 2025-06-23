class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Count frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Step 2: Sort characters by frequency (highest first)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Build result string
        result = ''
        for char, count in sorted_chars:
            result += char * count

        return result
