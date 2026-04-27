class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len(nums)-1
        i=0
        count =0
        for x in nums:
            if x!=val:
                nums[count] = x
                count+=1
        # while i < k:
        #     print("starting with ",nums[i]," and ",nums[k])
        #     while i<k and nums[i] != val:
        #         print("Finding val ",i+1)
        #         i+=1
        #     print("Found val elment at ",nums[i])
        #     while i<k and nums[k]==val:
        #         k-=1
        #     if i>=k:
        #         break
        #     print("Found Non-val elment at ",nums[k])
        #     print("Swapping")
        #     nums[i],nums[k] = nums[k],nums[i]
        #     print("New aarr ",nums)
        #     # k-=1
        #     # i+=1
        #     count+=1
        return count
        
s= Solution()
iin = [3,2,2,3]
i1 = [0,1,2,2,3,0,4,2]
k =s.removeElement(iin,3)
print(iin)
print(iin[:k])

print("---------------------------")
k = s.removeElement(i1,2)
print(i1)
print(i1[:k])