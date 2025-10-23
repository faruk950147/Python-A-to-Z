class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        print("\n")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")

    def make_move(self, position):
        """Player sets the position"""
        if self.board[position] == " ": # if the position is empty
            self.board[position] = self.current_player
            return True
        else:
            print("This position is already taken. Try again!")
            return False

    def check_winner(self):
        """Check if the current player has won"""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def switch_player(self):
        """Switch player"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def is_draw(self):
        """Check if the board is full"""
        return " " not in self.board # if the board is full

    def play(self):
        """Start the game"""
        print("Welcome to Tic Tac Toe (OOP Version)")
        self.print_board()

        while True:
            try:
                move = int(input(f"Player {self.current_player}, choose position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid position! Please choose between 1-9.")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue

            if self.make_move(move):
                self.print_board()

                if self.check_winner():
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.is_draw():
                    print("It's a draw!")
                    break

                self.switch_player()


# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
