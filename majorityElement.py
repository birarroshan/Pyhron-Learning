class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # mc = dict()
        # res= []
        # for x in nums:
        #     cc = mc.get(x,0)+1
        #     if cc>len(nums)//3:
        #         if x not in res:
        #             res.append(x)
        #         if len(res) ==2:
        #             break
        #     mc[x] = cc
        # return res

        n = len(nums)
        can1,can2 = None,None
        c1,c2 = 0,0

        for i in nums:
            if can1 == i:
                c1+=1
            elif can2 == i:
                c2+=1
            elif c1==0:
                can1 = i
                c1+=1
            elif c2==0:
                can2 = i
                c2+=1
            else:
                c1-=1
                c2-=1
            print(i,[can1,can2],c1,c2)
        res =[]
        for i in [can1,can2]:
            if nums.count(i)>=n//3:
                res.append(i)
        return res
s = Solution()
print(s.majorityElement([2,3,2,2,1,2,2,2,1]))