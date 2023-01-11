class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board), len(board[0])
        moves = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        next_steps = []

        for i in range(n):
            for j in range(m):
                neighbors_cells = 0
                for move in moves:
                    pos = (i + move[0], j + move[1])
                    if 0 <= pos[0] and pos[0] < n and 0 <= pos[1] and pos[1] < m and board[pos[0]][pos[1]]:
                        neighbors_cells += 1

                # live cell
                if board[i][j]:
                    if neighbors_cells < 2 or 3 < neighbors_cells:
                        # kill cell
                        next_steps.append(((i, j), 0))
                # dead cell
                else:
                    if neighbors_cells == 3:
                        # create cell
                        next_steps.append(((i, j), 1))

        # apply steps
        while next_steps:
            step = next_steps.pop()
            board[step[0][0]][step[0][1]] = step[1]