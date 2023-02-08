def check_row(board):
    """
    >>> check_row([  "**** ****","***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **","  8  2***","  2  ****"])
    True
    >>> check_row([  "**** ****","***1 ****", "**  3****", "* 4 *****", "     9 5 ", " 6  83  *", "3   1  **","  8  2***","  2  ****"])
    True
    >>> check_row([  "**** ****","**11 ****", "**  3****", "* 4 *****", "     9 5 ", " 6  83  *", "3   1  **","  8  2***","  2  ****"])
    False
    """
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = True
    for i in board:
        for j in i:
            if j in numbers and i.count(j) != 1:
                result = False
    return result

if __name__ == "__main__":
  import doctest
  print(doctest.testmod())
