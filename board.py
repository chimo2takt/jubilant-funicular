class TicTacToeBoard:

    def __init__(self):
        self.restart()

    def get(self, row:int, col:int):
        return f"{self._board[row][col]}"
    
    def is_empty(self, row:int, col:int):
        return True if self._board[row][col] == "-" else False

    def place(self, marker: str, row:int, col:int):
        if (marker == "X" or marker == "O") and self.is_empty(row,col):
            self._board[row][col] = marker
            return True
        else:  
            return False

    def print_board(self):
        for row in self._board:
            print(" ".join(row))

    def is_full(self):
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] == "-":
                    return False
        return True

    def restart(self):
        self._board = [["-" for _ in range(3)] for _ in range(3)]

    def is_winner(self, marker:  str):
        x = 0
        for row in range(len(self._board)): #Kollar radvis
            for col in range(len(self._board[row])):
                if marker == self.get(row,col):
                    x += 1
                    if x == 3:
                        return True
            x = 0

        for col in range(len(self._board[0])): #Kollar kolumnvis
            for row in range(len(self._board)):
                if marker == self.get(row,col):
                    x += 1
                    if x == 3:
                        return True
            x = 0

        if self.get(1,1) == marker: #Kollar diagonalvis
            if  (self.get(0,0) == marker) and  (self.get(2,2) == marker):
                return True
            elif (self.get(2,0) == marker) and (self.get(0,2) == marker):
                return True

        return False

if __name__ == '__main__':
    x = TicTacToeBoard()
    x.place('X',1,1)
    x.place('X',2,2)
    #x.place('X',2,0)
    x.print_board()
    print(x.is_winner('X'))