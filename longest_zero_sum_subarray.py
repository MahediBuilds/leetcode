class Solution:
    def longestSubarray(self, nums):
        # Write your solution here
        target = 0
        maxLen = 0
        prefixSum = {0: -1}
        currSum = 0

        for i, num in enumerate(nums):
            currSum += num
            diff = currSum - target

            if diff in prefixSum:
                maxLen = max(maxLen, i - prefixSum[diff])

            if currSum not in prefixSum:
                prefixSum[currSum] = i

        return maxLen


# ---------------- TESTING ----------------

solution = Solution()

nums = [9, -3, 3, -1, 6, -5]

result = solution.longestSubarray(nums)

print("Input:", nums)
print("Output:", result)
print("Expected:", 5)
