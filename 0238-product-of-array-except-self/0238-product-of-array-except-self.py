class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[1]*len(nums)
        right=[1]*len(nums)
        
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
            
        for j in range(len(nums)-2,-1,-1):
            right[j]=right[j+1]*nums[j+1]
           
        ans=[0]*len(nums)
        for i in range(len(nums)):
            ans[i]=left[i]*right[i]
            
        return ans    