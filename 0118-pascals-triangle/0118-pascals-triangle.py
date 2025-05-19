class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        k=[1]
        pas=[]
        pas.append(k)
        i=1
        while i<numRows:
            temp=[]
            check=pas[i-1]
            temp.append(check[0])
            if i>=2:
                for j in range(1,len(check),1):
                    temp.append(check[j]+check[j-1])
            temp.append(check[-1])
            i+=1
            pas.append(temp)
        return pas


        