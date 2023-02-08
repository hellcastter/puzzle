def columns_check(board: list[str]) -> bool:
    '''
    Transform the board and then check it in the check_row fnction
    >>> column_check([\
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
