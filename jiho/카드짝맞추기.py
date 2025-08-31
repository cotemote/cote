def get_perms():
    result = []

    def make_perm(acc):
        if len(acc) == 6:
            result.append(acc[:])
            return
        for i in range(1, 7):
            if i in acc:
                continue
            acc.append(i)
            make_perm(acc)
            acc.pop()

    make_perm([])
    return result


def find_pos(board, num):
    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == num:
                result.append((i, j))
    return result


def get_dist_by_bfs(board, start, end):
    if start == end:
        return 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[-1] * 4 for _ in range(4)]
    visited[start[0]][start[1]] = 0
    queue = [start]

    while len(queue) > 0:
        x = queue.pop(0)

        for d in dirs:
            I = x[0] + d[0]
            J = x[1] + d[1]
            if I < 0 or J < 0 or I >= 4 or J >= 4:
                continue
            if visited[I][J] != -1:
                continue
            visited[I][J] = visited[x[0]][x[1]] + 1
            queue.append((I, J))

        for d in dirs:
            I, J = x[0], x[1]
            while True:
                I += d[0]
                J += d[1]
                if I < 0 or J < 0 or I >= 4 or J >= 4:
                    I -= d[0]
                    J -= d[1]
                    break
                if board[I][J] != 0:
                    break
            if (I != x[0] or J != x[1]) and visited[I][J] == -1:
                visited[I][J] = visited[x[0]][x[1]] + 1
                queue.append((I, J))

    return visited[end[0]][end[1]]


def get_key_count(board, start_r, start_c, order):
    board_copy = [row[:] for row in board]
    cnt = 0
    cursor_pos = (start_r, start_c)

    for num in order:
        poses = find_pos(board_copy, num)
        if len(poses) < 2:
            continue

        pos1, pos2 = poses[0], poses[1]

        dist1 = get_dist_by_bfs(board_copy, cursor_pos, pos1)
        dist2 = get_dist_by_bfs(board_copy, pos1, pos2)
        path1_cost = dist1 + 1 + dist2 + 1

        dist3 = get_dist_by_bfs(board_copy, cursor_pos, pos2)
        dist4 = get_dist_by_bfs(board_copy, pos2, pos1)
        path2_cost = dist3 + 1 + dist4 + 1

        if path1_cost <= path2_cost:
            cnt += path1_cost
            cursor_pos = pos2
        else:
            cnt += path2_cost
            cursor_pos = pos1

        board_copy[pos1[0]][pos1[1]] = 0
        board_copy[pos2[0]][pos2[1]] = 0

    return cnt


def solution(board, r, c):
    cards = set()
    for row in board:
        for cell in row:
            if cell != 0:
                cards.add(cell)

    from itertools import permutations

    orders = list(permutations(cards))

    answer = float("inf")
    for order in orders:
        answer = min(answer, get_key_count([row[:] for row in board], r, c, order))

    return answer
