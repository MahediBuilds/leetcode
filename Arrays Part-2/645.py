class Solution:
    def findErrorNums(self, nums):
        seen = set()
        n = len(nums)
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num

            seen.add(num)

        actualSum = (n * (n + 1)) // 2
        uniqueSum = sum(seen)

        missing = actualSum - uniqueSum

        return [duplicate, missing]


nums = [1, 2, 2, 4]

solution = Solution()
result = solution.findErrorNums(nums)

print(result)
