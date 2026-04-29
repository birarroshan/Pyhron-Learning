class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        mc= 0
        for i in n:
            if (i-1) not in n:
                curr =i
                count=1
                #print("Curr and count",curr,count)
                while curr+1 in n:
                    count+=1
                    curr+=1
                    #print("Curr and count",curr,count)
                mc = max(mc,count)
        return mc

        
s =  Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))