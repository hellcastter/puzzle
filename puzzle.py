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

if __name__ == "__main__":
  import doctest
  print(doctest.testmod())
