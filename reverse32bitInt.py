class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31-1
        MIN_INT = -2**31

        if x == MIN_INT:
            return 0
        neg = 1
        if x <0:
            neg = -1
            x = x*-1
        num = 0
        while x >0:
            u = x % 10
            if MAX_INT//10 < num:
                return 0
            if neg == 1:
                if MAX_INT//10 == num and u>7:
                    return 0
            else:
                if MAX_INT//10 == num and u>8:
                    return 0
            num = num*10 +u
            x = x//10

        return num*neg

s = Solution()
# print(s.reverse(211))
print(s.reverse(-211))
# print(s.reverse(1534236469))
print(s.reverse(-2147483646))
print(s.reverse(7463847412))
print(s.reverse(8463847412))
print(s.reverse(-7463847412))
print(s.reverse(-8463847412))
