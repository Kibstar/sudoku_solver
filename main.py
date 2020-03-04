
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

s = '123456789123456789123456789123456789123456789123456789123456789123456789123456789'
s2 = '....717..1.2..25868.2388...129.9.89184...9488.7..3..161899.92.5.9.589.7942.72..12'
def string_to_list(s):
    main_list =[]
    sub_list = []
    for i, j in enumerate(s):
        if len(sub_list) == 9:
            main_list.append(sub_list)
            sub_list = []
        try:
            sub_list.append(int(j))
        except:
            sub_list.append(0)
    main_list.append(sub_list)
    return main_list


board2 = string_to_list(s2)


def print_puzzle(board):
    for y in range(len(board)):
        if y % 3 == 0 and y != 0:
            print('---------------------')
        for x in range(len(board[y])):
            if x % 3 == 0 and x != 0:
                print('| ',end='')
            if x != 8:
                print(f'{board[y][x]} ', end='')
            else:
                print(f'{board[y][x]} ')

def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                return y, x

    return False


def valid_check(board, num, yx):
    cur_y = yx[0]
    cur_x = yx[1]

    # check row

    for i in board[cur_y]:
        if i == num:
            return False

    # check col

    for i in board:
        if i[cur_x] == num:
            return False

    # check grid
    grid_y = (cur_y // 3) * 3
    grid_x = (cur_x // 3) * 3

    for i in range(grid_y,grid_y+3):
        for j in range(grid_x,grid_x+3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    next = find_empty(board)
    if next == False:
        return True
    else:
        y = next[0]
        x = next[1]
    for i in range(1,10):
        if valid_check(board,i,next):
            board[y][x] = i
            if solve(board):
                return True

    else:
        board[y][x] = 0
    return False


print_puzzle(board2)
