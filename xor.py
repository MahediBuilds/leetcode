class Solution:
    # Function to count subarrays with given XOR
    def countSubarrays(self, A, k):
        # Store frequency of prefix XORs
        prefixXor = {0: 1}
        currXor = 0
        diff = 0
        count = 0

        for num in A:
            currXor ^= num
            diff = currXor ^ k

            if diff in prefixXor:
                count += prefixXor[diff]
            prefixXor[currXor] = prefixXor.get(currXor, 0) + 1

        return count


# Driver code
A = [4, 2, 2, 6, 4]
k = 6
sol = Solution()
print(sol.countSubarrays(A, k))
