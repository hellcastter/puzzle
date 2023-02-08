def check_row(line: str) -> bool:
    """Check wheather in row only unique nums

    Args:
        line (str): board line

    Returns:
        bool: is valid
    
    >>> check_row("**** ****")
    True
    >>> check_row("* 4 1****")
    True
    >>> check_row("44** ****")
    False
    """
    for i in line:
        if i.isnumeric() and line.count(i) != 1:
            return False
            
    return True

def check_rows(board):
    """
    >>> check_rows([ \
        "**** ****", \
        "***1 ****", \
        "**  3****", \
        "* 4 1****", \
        "     9 5 ", \
        " 6  83  *", \
        "3   1  **", \
        "  8  2***", \
        "  2  ****" \
    ])
    True
    >>> check_rows([ \
        "**** ****", \
        "***1 ****", \
        "**  3****", \
        "* 4 *****", \
        "     9 5 ", \
        " 6  83  *", \
        "3   1  **", \
        "  8  2***", \
        "  2  ****" \
    ])
    True
    >>> check_rows([ \
        "**** ****", \
        "**11 ****", \
        "**  3****", \
        "* 4 *****", \
        "     9 5 ", \
        " 6  83  *", \
        "3   1  **", \
        "  8  2***", \
        "  2  ****" \
    ])
    False
    """
    return all([check_row(line) for line in board])

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
    >>> check_cells([\
        "**** ****",\
        "***1 ****",\
        "**  1****",\
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

        if not check_row(lst):
            return False
        
    return True

def validate_board(board: list[str]) -> bool:
    return False

if __name__ == "__main__":
  import doctest
  print(doctest.testmod())