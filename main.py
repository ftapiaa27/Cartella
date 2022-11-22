import random
class Game:
    alive = 1
    board_back = [[0 for i in range(9)] for j in range(9)]
    board_front = [["-" for i in range(9)] for j in range(9)]
    random_pairs = []
    x_coor = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    y_coor = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    print(x_coor, y_coor)
    for i in range(10):
        temp = []
        temp.append(x_coor.pop(random.choice(x_coor)))
        temp.append(y_coor.pop(random.choice(y_coor)))
        random_pairs.append(temp)
        board_back[temp[0]][temp[1]] = 1
    def print_board(self, board):
        for i in range(9):
            print(board[i])
    def set_flag(self):
        x = int(input("Type horizontal coordinate to flag: "))
        y = int(input("Type vertical coordinate to flag: "))
        self.board_front[y][x] = "F"
    def uncover(self):
        x = int(input("Type horizontal coordinate to uncover: "))
        y = int(input("Type vertical coordinate to uncover: "))
        if self.board_back[y][x] == 1:
            self.board_front[y][x] = "B"
            print("You lost")
            self.alive = 0
        self.board_front[y][x] = " "


game = Game()
while game.alive:
    game.print_board(game.board_back)
    game.print_board(game.board_front)
    choice = int(input("""
    Select one optione:
    1.- Flag
    2.- Uncover
    """))
    if choice == 1:
        game.set_flag()
    else:
        game.uncover()