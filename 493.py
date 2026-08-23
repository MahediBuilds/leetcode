class Solution:
    def reversePairs(self, nums):
        pairs = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    pairs += 1

        return pairs


nums = [1, 3, 2, 3, 1]

solution = Solution()
result = solution.reversePairs(nums)

print(result)
