class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[]
        for i in range(amount+1):
            dp.append(amount+1)

        dp[0]=0
        for i in range(len(dp)):
            for c in coins:
                if (i-c)>=0:
                    dp[i]=min(dp[i],dp[i-c]+1)
        if dp[amount]==amount+1:
            return -1
        else:
            return dp[amount]