from random import randrange

def display_board(board):
    for row in range(3):
        # Top border of each row
        print("+-------+-------+-------+")
        
        # First empty line with only vertical bars
        print("|       |       |       |")
        
        # Middle line with the values
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        
        # Another empty line with only vertical bars
        print("|       |       |       |")
    
    # Bottom border
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            User_Choice = int(input("Enter your move: "))
            
            # Check if the move is within valid range
            if User_Choice < 1 or User_Choice > 9:
                print("Invalid move! Please enter a number between 1 and 9.")
                continue
                
            # Convert the user's choice (1-9) to row and column coordinates
            row = (User_Choice - 1) // 3
            col = (User_Choice - 1) % 3
            
            # Check if the selected cell is free
            if board[row][col] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("That spot is already taken! Choose another.")
                continue
                
            # Update the board with the user's move (O)
            board[row][col] = 'O'
            return
            
        except ValueError:
            print("That's not a valid number! Try again.")

def make_list_of_free_fields(board):
    free_fields = []  # Create an empty list to store tuples of free positions
    
    # Loop through all positions on the board
    for row in range(3):
        for col in range(3):
            # Check if the current position contains a digit (is free)
            # Assuming free fields contain digits '1' through '9'
            if board[row][col] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                free_fields.append((row, col))  # Add the position as a tuple
                
    return free_fields  # Return the list of free positions


def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
            
    return False
    
def draw_move(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            # Check if the current position contains a digit (is free)
            # Assuming free fields contain digits '1' through '9'
            if board[row][col] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                free_fields.append((row, col))  # Add the position as a tuple
                
    if not free_fields:
        return
    
    choice = randrange(len(free_fields))
    row, col = free_fields[choice]
    
    board[row][col] = 'X'
    
def main():
    board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
    board[1][1] = 'X'
    free_fields = make_list_of_free_fields(board)
    
    while free_fields:
        display_board(board)
        
        # User's turn
        enter_move(board)
        
        if victory_for(board, 'O'):
            display_board(board)
            print("You won!")
            break
            
        # Update free fields
        free_fields = make_list_of_free_fields(board)
        
        # Check for a tie
        if len(free_fields) == 0:
            display_board(board)
            print("It's a tie!")
            break
            
        # Computer's turn
        draw_move(board)
        
        if victory_for(board, 'X'):
            display_board(board)
            print("Computer won!!!")
            break
        
        free_fields = make_list_of_free_fields(board)
          

if __name__ == "__main__":
    main()
        
    