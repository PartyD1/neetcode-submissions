"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s_intervals = sorted(intervals, key =lambda i:i.start)

        start = 0
        end = 0
        for inter in s_intervals:
            if  inter.start >= end:
                start = inter.start
            else:
                return False
            end = inter.end
        return True
            

