class Solution:
    def subarraySum(self, nums, k):

        result = 0
        currSum = 0
        prefixSum = {0: 1}

        for num in nums:
            currSum += num
            diff = currSum - k

            result += prefixSum.get(diff, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

        return result


nums = [1, 1, 1]
k = 2

solution = Solution()
result = solution.subarraySum(nums, k)

print(result)
