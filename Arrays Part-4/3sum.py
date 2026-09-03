class Solution:
    def threeSum(self, nums):
        target = 0
        res = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                numSum = num + nums[l] + nums[r]

                if numSum < target:
                    l += 1
                elif numSum > target:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
result = solution.threeSum(nums)

print(result)
