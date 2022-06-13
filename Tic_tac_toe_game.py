board = list(range(1, 10))

def draw_board(board):
    for i in range(3):
        print(board[0+i*3], board[1+i*3], board[2+i*3])

def play(xo):
    correct = False
    while not correct:
        answer = input("Куда поставим X или 0, введите номер клеточки:")
        try:
            answer = int(answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if answer >= 1 and answer <= 9:
            if str(board[answer - 1]) not in "XO":
                board[answer - 1] = xo
                correct = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Вы ввели не правильное число оно должно быть от 1 до 9")


def check_win(board):
    win_tuple = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for way in win_tuple:
        if board[way[0]] == board[way[1]] == board[way[2]]:
            return board[way[0]]
    else:
        return False


def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            play("X")
        else:
            play("O")
        count += 1
        if count > 4:
            if check_win(board):
                print(check_win(board), "Победа")
                win = True
                break
        if count == 9:
            print("Ничья")
            break
    draw_board(board)

main(board)
