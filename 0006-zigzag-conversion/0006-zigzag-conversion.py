class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
                # Edge case: if numRows is 1 or string is too short
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize rows as empty strings
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Build the zigzag pattern
        for char in s:
            rows[current_row] += char
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Combine all rows to get final string
        return ''.join(rows)


         
