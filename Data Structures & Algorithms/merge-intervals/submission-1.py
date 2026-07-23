class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_end = output[-1][1]
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]

            if cur_start <= prev_end:
                output[-1][1] = max(cur_end, prev_end)
            elif cur_start > prev_end:
                output.append(intervals[i])

        return output