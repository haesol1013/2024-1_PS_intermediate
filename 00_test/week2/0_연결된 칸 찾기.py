# 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0

    if visited[x][y] or grid[x][y] == 0:
        return 0

    visited[x][y] = True

    cnt = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cnt += dfs(x + dx, y + dy)

    return cnt


result = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j))

result.sort()
print(len(result))
for size in result:
    print(size)
