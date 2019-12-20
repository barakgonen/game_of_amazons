def get_col_index(column):
    print "<get_col_index()> Received column is: " + column + " ASCII of it is: " + str(ord(column))
    return ord(column) - ord('A')

def get_raw_index(raw_num, board_size):
    return board_size - raw_num