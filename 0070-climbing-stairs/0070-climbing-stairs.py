class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step=[]
        for i in range(n+1):
            step.append(0)
        meth=[1,2]
        step[0]=1
        for i in range(1,n+1):
            for m in meth:
                if i - m >= 0:
                    step[i] += step[i - m]

        return step[n]



        