class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1
                if cnt > 1:
                    ans+= i
            else:
                cnt -= 1
                if cnt > 0:
                    ans+= i
        return ans