class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])

        firstRowZero = False
        firstColumnZero = False

        # Row Check
        for n in range(columns):
            if matrix[0][n] == 0:
                firstRowZero = True
                break

        # Column Check
        for m in range(rows):
            if matrix[m][0] == 0:
                firstColumnZero = True
                break

        for m in range(1, rows):
            for n in range(1, columns):
                if matrix[m][n] == 0:
                    matrix[0][n] = 0
                    matrix[m][n] = 0

        for m in range(1, rows):
            for n in range(1, columns):
                if matrix[0][n] == 0 or matrix[m][0] == 0:
                    matrix[m][n] = 0

        if firstRowZero:
            for n in range(columns):
                matrix[0][n] = 0

        if firstColumnZero:
            for m in range(rows):
                matrix[m][0] = 0


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

solution = Solution()
solution.setZeroes(matrix)

print(matrix)
