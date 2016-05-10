# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda itv: (itv.start, itv.end))
        heap = []
        num_rooms = 1
        heapq.heappush(heap, intervals[0].end)
        for itv in intervals[1:]:
            if itv.start < heap[0]:
                heapq.heappush(heap, itv.end)
                num_rooms += 1
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, itv.end)
        return num_rooms


if __name__ == '__main__':
    itvs = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20),
    ]
    print(Solution().minMeetingRooms(itvs))
