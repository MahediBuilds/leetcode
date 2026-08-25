class Solution:

    def majorityElement(self, nums):
        cnt = 0
        ele = 0

        for num in nums:
            if cnt == 0:
                cnt += 1
                ele = num
            elif num == ele:
                cnt += 1
            else:
                cnt -= 1

        cnt = nums.count(ele)
        if cnt > (len(nums) // 2):
            return ele

        return -1


nums = [2, 2, 1, 1, 1, 2, 2]

solution = Solution()
result = solution.majorityElement(nums)

print(result)
