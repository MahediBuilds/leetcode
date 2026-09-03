class Solution:
    def majorityElement(self, nums):
        cnt1 = 0
        cnt2 = 0

        ele1 = float("-inf")
        ele2 = float("-inf")
        # ele2 = 0

        for num in nums:
            if cnt1 == 0 and num != ele2:
                cnt1 = 1
                ele1 = num
            elif cnt2 == 0 and num != ele1:
                cnt2 = 1
                ele2 = num
            elif ele1 == num:
                cnt1 += 1
            elif ele2 == num:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == ele1:
                cnt1 += 1
            if num == ele2:
                cnt2 += 1

        result = []
        check = len(nums) // 3
        if cnt1 > check:
            result.append(ele1)

        if cnt2 > check:
            result.append(ele2)
        return result


nums = [1, 2, 3, 1, 2, 1, 1]

solution = Solution()
result = solution.majorityElement(nums)

print(result)
