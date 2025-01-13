# Project: Enhancing Code Quality and Efficiency with ChatGPT

Welcome to a specialized module of our IT curriculum where we explore innovative ways to integrate artificial intelligence into everyday coding practices. This project focuses on debugging and automation in software development using ChatGPT to improve code quality and efficiency.

## Objectives
- **Debugging**: Understand how AI can help identify and solve coding errors.
- **Automation**: Learn to automate repetitive coding tasks using AI to enhance productivity.

## Outcomes
- **Enhanced Debugging Skills**: Troubleshoot and refine code effectively using AI-driven solutions.
- **Automation Proficiency**: Automate mundane tasks, creating error-free and structured code.

---

## Tasks

### 0. Debugging - Python Factorial
**Objective**: Use ChatGPT to identify and correct errors in code samples.

### Issue:
The code doesn't calculate the factorial correctly due to an infinite loop in the `factorial` function.

#### Fix:
```python
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result
Expected Output: The script should print the factorial of the input number.
1. Debugging - Python Arguments
Objective: Correct the code to ensure it prints only the arguments without the Python file name.

Issue:
The current implementation prints all arguments including the script name.

Fix:
python
Copier le code
for i in range(1, len(sys.argv)):  # Start from index 1 to exclude the script name
    print(sys.argv[i])
Expected Output: Only the arguments provided by the user should be printed, excluding the script name.
2. Debugging - HTML / Javascript
Objective: Correct the JavaScript code to change the background color when the button is clicked.

Issue:
The button's ID is incorrectly named "colorButon" instead of "colorButton", which causes the event listener to fail.

Fix:
html
Copier le code
<button id="colorButton">Change Color</button> <!-- Corrected the ID -->
<script>
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });
</script>
Expected Output: When the button is clicked, the background color of the page should change.
3. Debugging - Python Mines
Objective: Implement a mechanism to detect when all non-mine cells have been revealed to declare a win.

Issue:
The game doesn't have a condition to check when the user has revealed all non-mine cells.

Fix:
python
Copier le code
def check_victory(self):
    for y in range(self.height):
        for x in range(self.width):
            if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                return False
    return True

def play(self):
    while True:
        self.print_board()
        # User input and game continuation code...
        if self.check_victory():
            print("Congratulations! You've won the game.")
            break
Expected Output: When all non-mine cells are revealed, a victory message should be displayed.
4. Documentation - Python Factorial
Objective: Add appropriate comments to document the code.

Fix:
python
Copier le code
def factorial(n):
    """
    Function to calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
Expected Output: Comments should be added to explain the function, its parameters, and the return value.
5. Error Handling - Python Checkbook
Objective: Add error handling to prevent the program from crashing when invalid input is provided.

Issue:
The program crashes when a non-numeric value is entered for deposit or withdrawal.

Fix:
python
Copier le code
def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")
Expected Output: The program should handle invalid numeric inputs gracefully without crashing.
6. Debugging - Tic Tac Toe Python
Objective: Fix the errors and improve the game functionality.

Issue:
The game has logic errors such as announcing the winner after the last move by the losing player and missing input validation.

Fix:
python
Copier le code
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player
                    if check_winner(board):
                        print_board(board)
                        print(f"Player {player} wins!")
                        break
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input. Please enter a row and column between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
Expected Output: The game should validate inputs and correctly announce the winner.
Grading Criteria
Debugging Tasks (0-1 points each): For each debugging task, the solution should fix the identified problem and produce the correct output as described.
Documentation Tasks (0-1 point each): Code should be properly documented with clear and concise comments, including explanations of functions, parameters, and return values.
Error Handling Tasks (0-1 point each): Proper error handling should be implemented to ensure that the program does not crash due to invalid input.
Repository Structure
debugging/
factorial.py: Python script for calculating factorial.
print_arguments.py: Python script to print arguments.
change_background.html: HTML file for background color change.
mines.py: Python script for Minesweeper game.
factorial_recursive.py: Python script for recursive factorial calculation.
checkbook.py: Python script for managing a checkbook.
tic.py: Python script for Tic-Tac-Toe game.
Conclusion
By completing this project, you will learn how to leverage ChatGPT to enhance coding productivity, improve debugging skills, and implement automation for repetitive tasks. You'll gain a solid understanding of how AI can assist in software development and prepare you for future challenges in the tech industry.

css
Copier le code

Vous pouvez maintenant copier-coller ce texte dans un fichier `README.md` dans VS Code ou tout autre éditeur.
