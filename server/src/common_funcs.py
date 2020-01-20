import logging

def get_col_index(column, board_size):
    col_index = ord(column) - ord('A')
    logging.debug("<get_col_index()> Received column: " + str(column) + ", Calculated index: " + str(col_index))
    if (col_index < 0 or board_size < col_index):
        logging.error("<get_col_index()> Error, calculated index is out of bounds. Received column: " + str(column) + ", calculated index: " + str(col_index))
        raise IndexError('<get_col_index()> Col is invalid, we only have: ' + str(board_size) + ' columns, and you requested to get the index of col: ' + str(col_index))
    return col_index

def get_raw_index(raw_num, board_size):
    raw_index = board_size - raw_num
    logging.debug("<get_raw_index()> Received raw: " + str(raw_num) + ", Calculated index: " + str(raw_index))
    
    if (raw_index < 0 or board_size < raw_index):
        logging.error("<get_raw_index()> Error, calculated index is out of bounds. Received raw: " + str(raw_num) + ", calculated index: " + str(raw_index))
        raise IndexError('<get_raw_index()> Raw is invalid, we only have: ' + str(board_size) + ' rows, and you requested to get the index of raw: ' + str(raw_index))
    return raw_index