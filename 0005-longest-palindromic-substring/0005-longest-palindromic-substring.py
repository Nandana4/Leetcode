class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp=''
        max=0
        perm=''
        for i in range(len(s)):
            if len(s)<=1:
                return s
            for j in range(i+1,len(s)+1):
                temp=s[i:j]
                if temp==temp[::-1]:
                    if len(temp)>max:
                        max=len(temp)
                        perm=temp
                
        return perm

