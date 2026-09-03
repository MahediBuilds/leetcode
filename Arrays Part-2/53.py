class Solution:
    def merge(self, intervals):

        intervals.sort()

        i = 0
        while i < len(intervals) - 1:
            interval = intervals[i]
            nextInterval = intervals[i + 1]

            if nextInterval[0] in range(interval[0], interval[1] + 1):
                newInterval = [
                    min(interval[0], nextInterval[0]),
                    max(nextInterval[1], interval[1]),
                ]
                intervals.pop(i + 1)
                intervals[i] = newInterval
            else:
                i += 1

        return intervals


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

solution = Solution()
result = solution.merge(intervals)

print(result)
