class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,maxcount=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count=0
            maxcount=max(maxcount,count)   
        return maxcount