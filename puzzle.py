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

def columns_check(board: list[str]) -> bool:
    '''
    Transform the board and then check it in the check_row fnction
    >>> columns_check([\
        "**** ****",\
        "***1 ****",\
        "**  3****",\
        "* 4 1****",\
        "     9 5 ",\
        " 6  83  *",\
        "3   1  **",\
        "  8  2***",\
        "  2  ****"\
    ])
    False
    '''
    columns = [''.join([el[i] for el in board]) for i in range(len(board[0]))]
    return check_rows(columns)


def validate_board(board: list[str]) -> bool:
    """Validates board

    Args:
        board (list[str]): game board

    Returns:
        bool: is valid
        
    >>> validate_board([\
        "**** ****",\
        "***1 ****",\
        "**  3****",\
        "* 4 1****",\
        "     9 5 ",\
        " 6  83  *",\
        "3   1  **",\
        "  8  2***",\
        "  2  ****"\
    ])
    False
    >>> validate_board([\
        "**** ****",\
        "***1 ****",\
        "**  3****",\
        "* 4  ****",\
        "     9 5 ",\
        " 6  83  *",\
        "3   1  **",\
        "  8  2***",\
        "  2  ****"\
    ])
    True
    """
    if not check_rows(board):
        return False
    
    if not columns_check(board):
        return False
    
    if not check_cells(board):
        return False
    
    return True

if __name__ == "__main__":
  import doctest
  print(doctest.testmod())