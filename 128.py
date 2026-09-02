class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        numSet = set(nums)
        largest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                longest = 0
                while (num + longest) in numSet:
                    longest += 1
                largest = max(largest, longest)
        return largest


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

solution = Solution()
result = solution.longestConsecutive(nums)

print(result)
