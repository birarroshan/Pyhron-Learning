class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minstack = []
        answer = [0] * len(temperatures)
        for i,e in enumerate(temperatures):
            print(i,e)
            if not minstack:
                minstack.append([i,e])
             
            else :
                while minstack and e>minstack[-1][1]:
                    [j,f] = minstack.pop()
                    print("Popped ",j,f)
                    answer[j] = i-j
                minstack.append([i,e]) 
                print(minstack)                     
            print(answer)
            print("-"*50)
s = Solution()
s.dailyTemperatures([73,74,75,71,69,72,76,73])