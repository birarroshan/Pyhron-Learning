class Solution:
    def isPal(self, i, j, s):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        i = 0
        j = l-1
        while i<j:
            if s[i]!=s[j]:
                if (self.isPal(i+1,j,s) or  self.isPal(i,j-1,s)):
                    return True
                else:
                    False
            i+=1
            j-=1
        return False
    
s = Solution()
print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))