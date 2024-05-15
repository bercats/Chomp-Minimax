import copy

class ChocolateBar: #Class for the chocolate bar
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[1 for _ in range(cols)] for _ in range(rows)] #Create a grid of 1s with specified rows and columns
        self.grid[0][0] = -1  # Mark the poisonous square

    def remove_pieces(self, row, col): #Function to remove pieces from the chocolate bar to make a move
        for r in range(row, self.rows):
            for c in range(col, self.cols):
                self.grid[r][c] = 0

    def is_poisonous(self, row, col): #Function to check if the piece is poisonous
        return self.grid[row][col] == -1

    def is_terminal(self): #Function to check if the game is over
        return all(cell == 0 for row in self.grid for cell in row)

    def evaluate(self): #Function to evaluate the game state
        return sum(cell == 0 for row in self.grid for cell in row) #Return the number of eaten pieces

    def is_valid_move(self, row, col): #Function to check if the move is valid
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] != 0 #Check if the move is within the grid and the piece is uneaten

    def display(self): #Function to display the chocolate bar
        for row in self.grid:
            print(' '.join(['#' if cell == -1 else '0' if cell == 0 else '1' for cell in row])) #Print the chocolate bar with # for poisonous, 0 for eaten and 1 for uneaten
        print()

class Player: #Class for the player
    def __init__(self, name, is_human=True):  #Initialize the player with a name and whether it is human or AI
        self.name = name
        self.is_human = is_human
        self.visited_nodes = 0  # Initialize the counter for visited nodes

    def make_move(self, chocolate_bar): #Function to make a move
        if self.is_human:
            while True:
                try:
                    row, col = map(int, input("Enter row and column: ").split())
                    if chocolate_bar.is_valid_move(row, col):
                        return row, col
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")
        else:
            # AI move
            move = self.minimax_search(chocolate_bar, True)[1] #Get the best move using minimax search
            print(f"AI chooses move: {move}")  # Debug statement
            return move

    def minimax_search(self, chocolate_bar, is_max):
        self.visited_nodes += 1  # Increment the counter each time minimax_search is called

        #print(f"Visited nodes: {self.visited_nodes}")  # Debug statement
        #print(f"Entering minimax_search: is_max={is_max}")
        #chocolate_bar.display()


        if chocolate_bar.is_terminal(): #Check if the game is over
            evaluation = chocolate_bar.evaluate() #Evaluate the game state

            #print(f"Terminal state reached, evaluation={evaluation}")

            return evaluation, None

        if is_max: #If it is the maximizing player's turn, find the best move
            max_value = float('-inf')
            best_move = None
            for row in range(chocolate_bar.rows):
                for col in range(chocolate_bar.cols):
                    if chocolate_bar.is_valid_move(row, col):
                        simulated_bar = copy.deepcopy(chocolate_bar)
                        simulated_bar.remove_pieces(row, col)
                        value = self.minimax_search(simulated_bar, False)[0]
                        #print(f"Maximizing: tried move {(row, col)}, value={value}")
                        if value >= max_value:
                            max_value = value
                            best_move = (row, col)
            #print(f"Maximizing: best_move={best_move}, max_value={max_value}")
            return max_value, best_move
        else: #If it is the minimizing player's turn, find the worst move, this simulates the opponent's possible moves
            min_value = float('inf')
            for row in range(chocolate_bar.rows):
                for col in range(chocolate_bar.cols):
                    if chocolate_bar.is_valid_move(row, col):
                        simulated_bar = copy.deepcopy(chocolate_bar)
                        simulated_bar.remove_pieces(row, col)
                        value = self.minimax_search(simulated_bar, True)[0]
                        #print(f"Minimizing: tried move {(row, col)}, value={value}")
                        if value <= min_value:
                            min_value = value
            #print(f"Minimizing: min_value={min_value}")
            return min_value, None

class Game: #Class for the game
    def __init__(self, rows, cols, mode): #Initialize the game with the number of rows, columns and the mode
        self.chocolate_bar = ChocolateBar(rows, cols)
        self.players = self.setup_players(mode)
        self.current_player = 0

    def setup_players(self, mode): #Function to setup the players
        #display the chocolate bar
        print("Initial chocolate bar:")
        self.chocolate_bar.display()

        if mode == "AI": #If the mode is AI, ask the user if they want to start first
            human_first = input("Do you want to start first? (y/n): ").strip().lower() == 'y'
            if human_first:
                return [Player("Human", is_human=True), Player("AI", is_human=False)]
            else:
                return [Player("AI", is_human=False), Player("Human", is_human=True)]
        else:
            return [Player("Player 1", is_human=True), Player("Player 2", is_human=True)]

    def switch_player(self): #Function to switch the current player
        self.current_player = 1 - self.current_player

    def play(self): #Function to play the game
        while True:
            self.chocolate_bar.display() #Display the chocolate bar each turn
            current = self.players[self.current_player]
            print(f"{current.name}'s turn")
            row, col = current.make_move(self.chocolate_bar)
            if self.chocolate_bar.is_poisonous(row, col):
                print(f"{current.name} has to eat the poisonous piece! {self.players[1 - self.current_player].name} wins!")
                break
            self.chocolate_bar.remove_pieces(row, col)
            self.switch_player()
        for player in self.players:
            if not player.is_human:
                print(f"{player.name} visited {player.visited_nodes} nodes.")

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mode = input("Choose mode (AI/Human): ").strip()
    game = Game(rows, cols, mode)
    game.play()
