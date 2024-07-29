# 입력
n = int(input())
start_pos = tuple(map(lambda x: x-1, map(int, input().split())))
grid = [list(input()) for _ in range(n)]

# 방향 설정
start_direct = "r"
front = {"r": (0, 1), "d": (1, 0), "l": (0, -1), "u": (-1, 0)}
diagonal = {"r": (1, 1), "d": (1, -1), "l": (-1, -1), "u": (-1, 1)}

curr_pos, curr_direct = start_pos, start_direct


def can_out(pos):
    global n
    x, y = pos
    return x < 0 or x >= n or y < 0 or y >= n


def is_wall(pos):
    global grid
    x, y = pos
    return grid[x][y] == "#"


def is_same_state():
    global start_pos, curr_pos, start_direct, curr_direct
    return start_pos == curr_pos and start_direct == curr_direct


def rotate(direct, clockwise=False):
    directs = ["r", "d", "l", "u"]
    curr_idx = directs.index(direct)
    if clockwise:
        return directs[curr_idx+1] if curr_idx < 3 else directs[0]
    else:
        return directs[curr_idx-1] if curr_idx > 0 else directs[3]


cnt = 0
while True:
    front_pos = tuple(map(sum, zip(curr_pos, front[curr_direct])))
    diagonal_pos = tuple(map(sum, zip(curr_pos, diagonal[curr_direct])))

    if can_out(front_pos):
        cnt += 1
        print(cnt)
        break
    elif is_wall(front_pos):
        curr_direct = rotate(curr_direct)
    elif is_wall(diagonal_pos):
        cnt += 1
        curr_pos = front_pos
    else:
        cnt += 2
        curr_pos = diagonal_pos
        curr_direct = rotate(curr_direct, clockwise=True)

    if is_same_state():
        print(-1)
        break
