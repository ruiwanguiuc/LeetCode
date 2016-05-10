from collections import deque


def zombieCluster(zombies):
    """
    Computes the number of zombie clusters using BFS

    Args:
        zombies(list(str)): the matrix of connected zombies

    Returns:
        int
    """
    N = len(zombies)
    visited = [False] * N
    num_clusters = 0
    while True:
        queue = deque()
        # Take the first zombie that is not visited and do BFS starting at it
        for i in range(N):
            if not visited[i]:
                queue.append(i)
                break
        # if there is no zombie left that is not visited we are done
        if not queue:
            break
        # bfs
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            for i in range(N):
                if i != cur and not visited[i] and zombies[cur][i] == '1':
                    queue.append(i)
        # after bfs is done we are done with this cluster
        num_clusters += 1
    return num_clusters


if __name__ == '__main__':
    friends = [
        '1100',
        '1110',
        '0110',
        '0001'
    ]
    # friends = [
    #     'Y'
    # ]
    print(zombieCluster(friends))
