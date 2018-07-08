class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        d = {}
        for index, i in enumerate(s):
            if i in d and d[i] >= left:
                left = d[i] + 1
            d[i] = index
            res = max(res, index - left + 1)
        return res
