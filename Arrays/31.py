class Solution:
    def nextPermutation(self, nums):
        index = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return nums

        for i in range(index + 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        nums[index + 1 :] = reversed(nums[index + 1 :])

        return nums


nums = [2, 3, 1]

solution = Solution()
solution.nextPermutation(nums)

print(nums)
