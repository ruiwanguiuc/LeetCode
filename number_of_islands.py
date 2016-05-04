from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            while q:
                curx, cury = q.popleft()
                grid[curx][cury] = 'X'
                for nextx, nexty in (
                    (curx + 1, cury + 1),
                    (curx + 1, cury - 1),
                    (curx - 1, cury + 1),
                    (curx - 1, cury - 1),
                ):
                    if nextx >= 0 and nexty >= 0 and nextx < row and nexty < col:
                        if grid[nextx][nexty] == '1':
                            q.append((nextx, nexty))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        return count


if __name__ == "__main__":
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    print(Solution().numIslands(grid))
