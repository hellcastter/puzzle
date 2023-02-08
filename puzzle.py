def check_cells(board):
    size = len(board)

    for angle in range(5):
        lst = []

        for i in range(5):
            lst += board[size - angle - i - 1][angle]
            lst += board[size - angle - 1][angle + i]
        lst.pop(0)
        return check_row(lst)
