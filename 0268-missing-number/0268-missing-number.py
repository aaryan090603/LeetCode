class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        c=[]
        for i in range(0,n+1):
            c.append(i)
            i+=1
        return sum(c)-sum(nums)    