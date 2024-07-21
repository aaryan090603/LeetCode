class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ''
        for i in s:
            if i.isalpha() or i.isnumeric():
                s1 += i
        return s1 == s1[::-1]