class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        idx = -1
        records = []
        for i in operations:
            if i == "+":
                sum += records[idx]+records[idx-1]
                records.append(records[idx]+records[idx-1])
                idx+=1
            elif i == "D":
                sum += records[idx]*2 
                records.append(records[idx]*2)
                idx+=1
            elif i == "C":
                sum-=records[idx]
                records.pop(idx)
                idx-=1
            else:
                sum+=int(i)
                records.append(int(i))
                idx+=1
                
            print("Records - ",records)

inp =["5","2","C","D","+"]
s = Solution()
print(s.calPoints(inp))