class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        openParenthesis = []
        res = []

        for c in s:
            if c=='(':
                openParenthesis.append(len(res))
            elif c==')':
                start = openParenthesis.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(c)
        return ''.join(res)