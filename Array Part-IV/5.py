class Solution:
    def lengthOfLongestSubstring(self, s):

        cSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[r])
                l += 1
            cSet.add(s[r])
            res = max(res, r - l + 1)

        return res


s = "abcabcbb"

solution = Solution()
result = solution.lengthOfLongestSubstring(s)

print(result)
