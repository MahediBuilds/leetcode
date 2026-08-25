class Solution:

    def myPow(self, x, n):

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)
        else:
            half = self.myPow(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x


x = 2
n = 0

solution = Solution()
result = solution.myPow(x, n)

print(result)
