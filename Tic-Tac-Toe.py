import pygame
pygame.init()

width = height = 600
square = int(width / 3)
lines_width = 10
o_size = int(square // 4)
space = int(square // 4)
background_color = (4, 60, 83)
lines_color = text_color = (255, 255, 255)
x_color = (4, 21, 28)
o_color = (255, 255, 255)
last_char = ' '
mouse_clicked = False
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
#Set size to the screen
screen = pygame.display.set_mode((width, height))
#Set Game caption
pygame.display.set_caption("Play multiplayer Tic Tac Toe game")
#Set Color to the screen background
screen.fill(background_color)

#Drawing the body of the game
def draw_lines():
    #first verticle line
    pygame.draw.line(screen, lines_color, (square, 0), (square, height), lines_width)
    #2nd verticle line
    pygame.draw.line(screen, lines_color, (square*2, 0), (square*2, height), lines_width)
    #first horizontal line
    pygame.draw.line(screen, lines_color, (0, square), (width, square), lines_width)
    #2nd horizontal line
    pygame.draw.line(screen, lines_color, (0, square*2), (width, square*2), lines_width)
#Check if a player has won
def is_winning(board):
    character = 'T'
    if character == 'T':
        for row in range (len(board)):
            if board[row][0] == board[row][1] == board[row][2]:
                if board[row][0] == 'x':
                    character = 'X'
                    draw_horizontal_win(row, 'x')
                elif board[row][0] == 'o':
                    character = 'O'
                    draw_horizontal_win(row, 'o')
                else:
                    character = 'T'
    if character == 'T':
        for col in range(len(board)):
            if board[0][col] == board[1][col] == board[2][col]:
                if board[0][col] == 'x':
                    character = 'X'
                    draw_verticle_win(col, 'x')
                elif board[0][col] == 'o':
                    character = 'O'
                    draw_verticle_win(col, 'o')
                else:
                    character = 'T'
    # Check the main diagonal
    if character == 'T':
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'x':
                character = 'X'
                draw_normal_diagonal_win('x')
            elif board[0][0] == 'o':
                character = 'O'
                draw_normal_diagonal_win('o')
            else:
                character = 'T'
    # Check the revers diagonal
    if character == 'T':
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'x':
                character = 'X'
                draw_reverse_diagonal_win('x')
            elif board[0][2] == 'o':
                character = 'O'
                draw_reverse_diagonal_win('o')
            else:
                character = 'T'
    if is_board_full() and character == 'T':
        character = "TIE"
    return character
#Modifying the 2d Array board with every turn
def insert(board, char, row, column):
    global last_char
    if mouse_clicked == False:
        if 0 <= row < 3 and 0 <= column < 3:
            if board[row][column] == " ":
                if char == 'x' and last_char != 'x':
                    board[row][column] = 'x'
                    last_char = 'x'
                    return True
                elif char == "o" and last_char != 'o':
                    board[row][column] = "o"
                    last_char = 'o'
                    return True
                else:
                    print("Invalid character/turn! please type either X or O with respect to turn!")
                    return False
            else:
                print("This Cell is not empty!")
                return False
        else:
            print("row and column values must be less than 3 and greater than 0!")
    else:
        if board[row][column] == " ":
            if char == 'x' and last_char != 'x':
                board[row][column] = 'x'
                last_char = 'x'
                return True
            elif char == 'x' and last_char == 'x':
                board[row][column] = 'o'
                last_char = 'o'
                return True
            elif char == "o" and last_char != 'o':
                board[row][column] = "o"
                last_char = 'o'
                return True
            elif char == "o" and last_char == 'o':
                board[row][column] = "x"
                last_char = 'x'
                return True
        else:
            print("This Cell is not empty!")
            return False
#Prints the current game board on screen
def print_board():
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 'o':
                pygame.draw.circle(screen, o_color, (int(column * square + square/2), int(row * square + square/2)), o_size, 15)
            elif board[row][column] == 'x':
                pygame.draw.line(screen, x_color, (int(column * square + square - space), int(row * square + space)), (int(column * square + space), int(row * square + square - space)), 25)
                pygame.draw.line(screen, x_color, (int(column * square + space), int(row * square + space)), (int(column * square + square - space), int(row * square + square - space)), 25)

def main():
    running = True
    while running:
        pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.event.pump()
        char = input("Enter the character: ")
        row = int(input("Enter the row: "))
        column = int(input("Enter the column: "))
        insert(board, char, row, column)
        print_board()
        char = is_winning(board)
        if char == 'X':
            print("Player X wins!")
            running = False
        elif char == 'O':
            print("player O Wins!")
            running = False
        elif char == "TIE":
            print("No one Wins, TIE!")
            running = False
        pygame.display.update()
        pygame.time.wait(3000)
    pygame.time.wait(2000)
    pygame.quit()
def is_board_full():
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == ' ':
                return False
    return True
def draw_verticle_win(col, char):
    x = col * square + square/2
    if char == 'x':
        color = x_color
    elif char == 'o':
        color = o_color
    pygame.draw.line(screen, color, (x, 10), (x, height - 10), 20)
def draw_horizontal_win(row, char):
    y = row * square + square/2
    if char == 'x':
        color = x_color
    elif char == 'o':
        color = o_color
    pygame.draw.line(screen, color, (10, y), (width - 10, y), 20)
def draw_normal_diagonal_win(char):
    x = 10
    y = 10
    end_x = width - 10
    end_y = height - 10
    if char == 'x':
        color = x_color
    elif char == 'o':
        color = o_color
    pygame.draw.line(screen, color, (x, y), (end_x, end_y), 20)
def draw_reverse_diagonal_win(char):
    x = width - 10
    y = 10
    end_x = 10
    end_y = height - 10
    if char == 'x':
        color = x_color
    elif char == 'o':
        color = o_color
    pygame.draw.line(screen, color, (x, y), (end_x, end_y), 20)
def play_with_mouse():
    running = True
    global mouse_clicked
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
                x = event.pos[0]
                y = event.pos[1]
                clicked_r = int(y // square)
                clicked_c = int(x // square)
                insert(board, 'x', clicked_r, clicked_c)
                print_board()
                char = is_winning(board)
                if char == 'X':
                    print("Player X wins!")
                    running = False
                elif char == 'O':
                    print("player O Wins!")
                    running = False
                elif char == "TIE":
                    print("No one Wins, TIE!")
                    running = False
        pygame.event.pump()
        pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
draw_lines()
pygame.display.update()
print(int(10.8))
control = input("Choose controller: [mouse(m) or keyboard(k)]: ")
if control == 'm' or control == "mouse":
    print("Play with your mouse")
    play_with_mouse()
else:
    print("Play with your keyboard by inserting the position and character")
    main()
