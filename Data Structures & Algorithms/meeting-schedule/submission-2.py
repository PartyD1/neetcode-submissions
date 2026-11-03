class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)

        end = 0

        for inter in intervals:
            if inter.start >= end:
                end = inter.end
            else:
                return False

        return True