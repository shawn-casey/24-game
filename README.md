24 Game Solver

The 24 Game Solver is a Python program that finds all possible solutions for the 24 game using a user-provided set of four cards. The 24 game is a mathematical puzzle in which the objective is to use the four numbers on the cards, along with the basic arithmetic operations (+, -, *, /), to obtain the value of 24.

Requirements: Python

Usage
1. Copy and paste the code into a Python environment or a Python file (e.g., solver.py).
2. Run the script.
3. Enter the four cards separated by spaces when prompted. For example, 2 4 6 8.
4. The program will calculate and display all possible solutions for the 24 game using the provided cards.

Code Explanation
The code consists of two classes: BETNode and the main program.

BETNode Class
The BETNode class represents a node in a binary expression tree (BET) used to evaluate arithmetic expressions. It has the following methods:

- __init__(self, value, left=None, right=None): Initializes a BETNode object with a value and optional left and right child nodes.
- __eq__(self, other): Compares two BETNode objects for equality.
- __hash__(self): Computes the hash value of a BETNode object.
- add_left(self, node): Sets the left child of the node.
- add_right(self, node): Sets the right child of the node.
- evaluate(self): Evaluates the arithmetic expression represented by the BETNode object.
- __repr__(self): Returns a string representation of the BETNode object.

create_trees(cards) Function
The create_trees(cards) function generates all possible arithmetic expressions using the given cards and operators. It returns a set of valid BETNode objects representing the expressions.

find_solutions() Function
The find_solutions() function prompts the user to enter four cards and finds all possible solutions for the 24 game using the provided cards. It utilizes the create_trees(cards) function to generate valid expressions and checks if their evaluated value is 24.

Example
"""
Enter the four cards (separated by spaces): 2 4 6 8
Possible solutions:
((2 + 4) * (6 - 8))
((6 - 8) * (2 + 4))
"""
This example shows the output when the user enters the cards 2, 4, 6, and 8. The program finds two possible solutions for the 24 game using these cards.
Note: The solutions may vary depending on the input cards.
