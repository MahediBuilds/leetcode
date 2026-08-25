class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):
            x = target - num

            if x in seen:
                return [seen[x], i]

            seen[num] = i


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)

print(result)
