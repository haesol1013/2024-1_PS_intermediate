# 입력
t = int(input())


# 벽 감지
def detect_wall(x, y):
    global n
    return x < 0 or x >= n or y < 0 or y >= n


# 이동
def move(x, y, direct):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    next_x, next_y = x + dxs[direct], y + dys[direct]

    if detect_wall(next_x, next_y):
        direct = (direct + 2) % 4
        return x, y, direct
    else:
        return next_y, next_y, direct


def one_cycle(bombs):
    for i, bomb in enumerate(bombs):
        bombs[i] = move(*bomb)

    exited_bomb = set()
    del_list = set()

    for bomb in bombs:
        if bomb[:2] not in exited_bomb:
            exited_bomb.add(bomb[:2])
        else:
            del_list.add(bomb[:2])

    bombs = [bomb for bomb in bombs if bomb[:2] not in del_list]
    return bombs


def simulate(bombs):
    while True:
        bombs = one_cycle(bombs)

        if not detect_collision(bombs):
            break

        if not bombs:
            break

    return len(bombs)


def convert(bombs):
    direct_dict = {"R": 0, "D": 1, "L": 2, "U": 3}

    for i, bomb in enumerate(bombs):
        x, y = int(bomb[0]) - 1, int(bomb[1]) - 1
        direct = direct_dict[bomb[2]]
        bombs[i] = [x, y, direct]

    return bombs


def detect_collision(bombs):
    rows = {}
    cols = {}

    for x, y, _ in bombs:
        if x in rows:
            rows[x].append(y)
        else:
            rows[x] = [y]

        if y in cols:
            cols[y].append(x)
        else:
            cols[y] = [x]

    for row in rows.values():
        if len(row) > 1:
            return True

    for col in cols.values():
        if len(col) > 1:
            return True

    return False


for _ in range(t):
    n, m = map(int, input().split())
    bombs = [
        input().split()
        for _ in range(m)
    ]
    bombs = convert(bombs)
    print(simulate(bombs))
