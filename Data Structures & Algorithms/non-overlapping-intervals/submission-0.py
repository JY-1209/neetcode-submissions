class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = intervals.sort(key = lambda x: x[1])
        prev_end = intervals[0][1]
        remove = 0

        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if prev_end > cur_interval[0]:
                remove += 1
            else:
                prev_end = cur_interval[1]

        return remove