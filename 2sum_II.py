class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        numbers.sort()

        while l < r:
            numSum = numbers[l] + numbers[r]

            if numSum < target:
                l += 1
            elif numSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return [-1, -1]


numbers = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(numbers, target)

print(result)
