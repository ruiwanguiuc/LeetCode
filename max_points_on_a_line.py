# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


from collections import defaultdict


def get_slope(p1, p2):
    if p1.x == p2.x and p1.y == p2.y:
        return None
    if p1.x == p2.x:
        return 'Inf'
    return (p1.y - p2.y) / float((p1.x - p2.x))


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) == 1:
            return 1
        max_points = 0
        for i in range(len(points)):
            count_by_slope = defaultdict(int)
            same_point_count = 0
            cur_max = 0
            for j in range(len(points)):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same_point_count += 1
                else:
                    slope = get_slope(points[i], points[j])
                    count_by_slope[slope] += 1
                    cur_max = max(cur_max, count_by_slope[slope])
            max_points = max(max_points, cur_max + same_point_count + 1)
        return max_points


if __name__ == "__main__":
    points = [
        Point(0, 0),
        Point(1, 0),
        Point(1, 1),
        Point(1, 1),
        Point(2, 2),
    ]
    print(Solution().maxPoints(points))
