class Solution:
    def maxSubArray(self, nums):
        largest = float("-inf")
        sum = 0

        for num in nums:
            sum += num

            largest = max(largest, sum)
            sum = max(sum, 0)

        return largest


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()
result = solution.maxSubArray(nums)

print(result)
