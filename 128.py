class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        numSet = set(nums)

        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

solution = Solution()
result = solution.longestConsecutive(nums)

print(result)
