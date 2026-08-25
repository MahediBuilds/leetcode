class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = n - 1

                while l < r:
                    fourS = nums[i] + nums[j] + nums[l] + nums[r]

                    if fourS < target:
                        l += 1
                    elif fourS > target:
                        r -= 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])

                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        return result


nums = [1, 0, -1, 0, -2, 2]
target = 0

solution = Solution()
result = solution.fourSum(nums, target)

print(result)
