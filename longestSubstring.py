class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in window:
                left = max(left,window[ch]+1)
            window[ch] = right
            max_len = max(max_len,right-left+1)   
        return max_len
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
