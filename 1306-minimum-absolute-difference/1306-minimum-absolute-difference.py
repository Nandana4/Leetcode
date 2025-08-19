class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        arr=sorted(arr)
        min_diff=float('inf')

        for i in range(1,len(arr)):
            min_diff=min(min_diff,arr[i]-arr[i-1])
        
        for i in range(1,len(arr)):
            if min_diff==arr[i]-arr[i-1]:
                result.append([arr[i-1],arr[i]])
        return result 
