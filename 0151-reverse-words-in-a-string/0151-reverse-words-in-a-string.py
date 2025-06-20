class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new=[]
        s=s.lstrip()
        s=s.rstrip()
        words=s.split(' ')
        for word in words:
            if word !='':
                new.append(word)
        new=new[::-1]
        result=""
        for j in range(len(new)):
            if j ==len(new)-1:
                result+=(new[j])
            else:
                result+=(new[j])
                result+=(' ')
        return result