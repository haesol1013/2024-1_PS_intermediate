n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]


def explode_bombs(n, m, bombs):
    while True:
        new_bombs = []
        i = 0
        exploded = False

        while i < len(bombs):
            start = i
            while i < len(bombs) and bombs[start] == bombs[i]:
                i += 1

            if i - start >= m:
                exploded = True
            else:
                new_bombs.extend(bombs[start:i])

        if not exploded:
            break

        bombs = new_bombs

    return bombs


result_bombs = explode_bombs(n, m, bombs)

print(len(result_bombs))
for bomb in result_bombs:
    print(bomb)
