class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        c=[0,1]
        for i in range(2,n+1):
            value=c[i-1]+c[i-2]
            c.append(value)
        return c[-1]  