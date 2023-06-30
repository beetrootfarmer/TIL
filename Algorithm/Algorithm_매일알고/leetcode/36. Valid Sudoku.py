def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # 스토쿠 리스트의 가로, 세로, 9개의 사각형을 검증하여 1~9가 중복되지 않는지 확인
    result = True

    # 가
    for row in range(9):
        # 줄 별로 중복 숫자가 없는지 확인
        for col in range(9):

            if board[row][col] != '.' and board[row].count(board[row][col]) > 1:
                result = False
                break
            # 사각형 확인 : 사각형 좌측 모서리를 기준으로 숫자를 담아서 중복이 없는지 확인
            if row in (0,3,6) and col in (0,3,6):
                box = []
                for s in range(row, row+3):
                    for e in range(col, col+3):
                        if box and board[s][e] in box:
                            result = False
                            break
                        if board[s][e] != '.':
                            box.append(board[s][e])
                    if not result: break
            if not result: break
        if not result: break
    if result:
    # zip으로 전환 후 세로
        board2 = list(map(list, zip(*board)))
        for row in range(9):
            for col in range(9):
                if board2[row][col] != '.' and board2[row].count(board2[row][col]) > 1:
                    result = False
                    break
            if result == False:
                break
        if not result:
            return 'false'
    if result:
        return 'true'

a = isValidSudoku(
[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
)
print(a)

