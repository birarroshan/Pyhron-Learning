class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = False
        i = len(a)-1
        j = len(b)-1
        # a_ch = ""
        # b_ch = ""
        while i >= 0 or j >= 0:
           
            if i>=0:
                a_ch = a[i]
                i-=1
            else: 
                a_ch = "0"

            if j>=0:
                b_ch = b[j]
                j-=1
            else: 
                b_ch = "0"
            if a_ch == "0" and b_ch == "0":
                if carry:
                    res.append("1")
                    carry = False
                else: 
                    res.append("0")
            elif a_ch == "1" and b_ch == "1":
                if carry:
                    res.append("1")
                else:
                    res.append("0")
                    carry = True
            else: 
                if carry:
                    res.append("0")
                    # Let carry go ahead
                    #carry = False
                else: 
                    res.append("1")
        if carry:
            res.append("1")
        return "".join(res[::-1])
    
s = Solution()
a= "1101"
b = "101"
print(a)
print(b)
print(s.addBinary(a,b))