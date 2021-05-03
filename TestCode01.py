board = [[3,0,0,2],
         [0,0,1,0],
         [0,1,0,0],
         [2,0,0,3]]
#r = y
#c = x

def solution(board, r, c):
    real_pos_value = board[r][c]
    real_pos_y = r
    real_pos_x = c

    print("Cursor :", real_pos_y, real_pos_x, "Value :",real_pos_value)
    ############  초기 좌표 설정 부분  ############
    if real_pos_value == 0:
        for x in range(4):
            if board[real_pos_y][x] != 0:
                real_pos_x = x
                break

    if real_pos_value == 0:
        for y in range(4):
            if board[y][real_pos_x] != 0:
                real_pos_y = y
                break
    # Y, X축 둘다 없을경우 초기좌표 찾아가는 함수 만들어야함

    real_pos_value = board[real_pos_y][real_pos_x]
    print("Cursor :", real_pos_y, real_pos_x, "Value :",real_pos_value)
    ###############################################

    for y in range(4):
        for x in range(4):
            if board[y][x] == real_pos_value:
                print("Search Value :",real_pos_value,"Searched POS :",y,x)

    #return answer

solution(board,0,1)
