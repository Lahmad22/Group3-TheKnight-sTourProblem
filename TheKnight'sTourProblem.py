# Python Code for Knights Tour Problem
# Using Recursion + Backtracking

def isSafe(x, y, n, board):
    return x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1

def knightTourUtil(x, y, step, n, board, dx, dy):
    # If all squares are visited
    if step == n * n:
        return True

    # Try all 8 possible knight moves
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if isSafe(nx, ny, n, board):
            board[nx][ny] = step

            if knightTourUtil(nx, ny, step + 1, n, board, dx, dy):
                return True

            # Backtrack
            board[nx][ny] = -1

    return False

def knightTour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # 8 directions of knight moves
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

# Start from top-left corner
    board[0][0] = 0

    if knightTourUtil(0, 0, 1, n, board, dx, dy):
        return board

    return [[-1]]

def printBoard(board):
    n = len(board)
    for row in board:
        for val in row:
            # print numbers aligned (e.g., 2-digit boards still look neat)
            print(f"{val:2}", end=" ")
        print()

if _name=="main_":
    n = 5  # change board size here
    res = knightTour(n)

    if res[0][0] == -1:
        print("No solution found.")
    else:
        print(f"Knight’s Tour solution for {n}x{n} board:\n")
        printBoard(res)
