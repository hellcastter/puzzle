def check_cells(board):
    """
    >>> check_cells(["**** ****",\
        "***1 ****",\
        "**  3****",\
        "* 4 1****",\
        "     9 5 ",\
        " 6  83  *",\
        "3   1  **",\
        "  8  2***",\
        "  2  ****"])
    True
    >>> check_cells(["**** ****",\
        "***1 ****",\
        "**  3****",\
        "* 4 1****",\
        "     9 5 ",\
        " 6  83  *",\
        "3   1  **",\
        "  8  2***",\
        "  2  ****"])
    False
    """
    size = len(board)

    for angle in range(5):
        lst = []

        for i in range(5):
            lst += board[size - angle - i - 1][angle]
            lst += board[size - angle - 1][angle + i]
        lst.pop(0)
        return check_row(lst)
