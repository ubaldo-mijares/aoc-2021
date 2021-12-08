

def bingo_check(board_dict, number, no_of_boards):

    score = 'none'
    
    # create a list of boards to delete
    delete_board = list()

    for board in board_dict:

        for row in board_dict[board]:

            # check if the number is in the row
            try:
                index_search = row.index(number)

                # mark the spot on the bingo board
                row[index_search] = 'x'

            except ValueError:
                continue
    
            # check if any rows are winners, sum everything up and multiply by the current number
            if len(set(row)) == 1:

                if no_of_boards == 1:

                    row_sum = list()

                    for row in board_dict[board]:
                        row_sum.append(sum([val for val in row if val != 'x']))

                    score = sum(row_sum) * number

                    print(f'Score is: {score}')
                    return False, score

                else:

                    delete_board.append(board)
                    break

        # need lists to check columns
        col_dict = {val: [] for val in range(1,6)}

        # check if any columns are winners
        for val in board_dict[board]:

            col_dict[1].append(val[0])
            col_dict[2].append(val[1])
            col_dict[3].append(val[2])
            col_dict[4].append(val[3])
            col_dict[5].append(val[4])
        
        for key in col_dict:

            if len(set(col_dict[key])) == 1:

                if no_of_boards == 1:

                    row_sum = list()

                    for row in board_dict[board]:
                        row_sum.append(sum([val for val in row if val != 'x']))

                    score = sum(row_sum) * number
                    print(f'Score is: {score}')
                    return False, score

                else:

                    delete_board.append(board)
                    break
    
    return delete_board, score


def main():
    '''
        function to figure out how much power the sub consumes
    '''

    # ingest the list of items
    with open('Ubaldo/problem4.txt') as txt:
        puzzle_input = txt.read().splitlines()

    # the first line is the drawings for bingo
    drawings = puzzle_input[0].split(',')
    drawings = [int(val) for val in drawings]

    # separate the bingo boards out into 2D arrays
    # the boards are 5x5, and they are separated by blank lines
    boards = [val for val in puzzle_input[2:] if val != '']
    board_dict = dict()
    
    group_counts = int(len(boards)/5)

    for iterator in range(0, group_counts):

        board_dict[iterator] = boards[iterator * 5:iterator * 5 + 5]

        # split each row into a list of numbers
        for index, item in enumerate(board_dict[iterator]):

            item = item.split(" ")
            board_dict[iterator][index] = [int(val) for val in item if val != ""]
    
    delete_board = []
    # go through the drawing numbers and check for a winning board
    for number in drawings:

        if delete_board:

            for val in delete_board:
                try:
                    del board_dict[val]
                except KeyError:
                    continue

        no_of_boards = len(board_dict)

        delete_board, score = bingo_check(board_dict, number, no_of_boards)

        if score != 'none':
            return

# run it
if __name__ == '__main__':

    main()