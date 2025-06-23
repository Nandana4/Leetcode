class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth=0
        maxd=0
        for i in s:
            if i=='(':
                depth+=1
            if i==')':
                depth-=1
            maxd=max(depth,maxd)
        return maxd
        
