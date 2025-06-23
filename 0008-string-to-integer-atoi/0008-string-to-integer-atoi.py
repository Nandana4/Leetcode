class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip() 
        if not s:
            return 0

        i = 0
        sign = 1
        total = 0

        if s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            total = total * 10 + int(s[i])
            i += 1

        total *= sign

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if total < INT_MIN:
            return INT_MIN
        if total > INT_MAX:
            return INT_MAX
        return total
