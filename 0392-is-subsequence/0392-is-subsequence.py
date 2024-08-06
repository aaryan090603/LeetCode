class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slow = 0
        if len(s) == 0:
            return True
        for fast in range(len(t)):
            if s[slow] == t[fast]:
                slow += 1
            if slow == len(s):
                return True
        return False
