class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=[]
        nums=Counter(nums)
        nums=list(Counter(nums).items())
        nums.sort(key=lambda x:(x[1],-x[0]))
        for i,j in nums:
            b.extend([i]*j)
        return b