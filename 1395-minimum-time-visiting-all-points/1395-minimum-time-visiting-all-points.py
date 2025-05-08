class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=0
        x1,y1=points.pop()
        while points:
            x2,y2=points.pop()
            res+=max(abs(x1-x2),abs(y1-y2))
            x1, y1 = x2, y2
        return res 

        