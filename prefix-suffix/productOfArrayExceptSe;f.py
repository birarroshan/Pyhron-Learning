class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lres= [1]*l 
        suffix =1
        for i in range(1,l):
            lres[i] = nums[i-1] * lres[i-1]
        for i in range(l-2,-1,-1):
            suffix = nums[i+1] * suffix
            lres[i] = lres[i]*suffix

        prefix = 1
        for i in range(l):
            lres[i] =  prefix
            prefix *=nums[i]

        suffix = 1
        for i in range(l-1,-1,-1):
            lres[i] = lres[i]*suffix
            suffix = suffix * nums[i]
        return lres