from itertools import product, permutations


class BETNode:
    """Node for binary expression tree"""
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A': 1, '1': 1, '2': 2, '3': 3, '4': 4,
                     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                     '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))

    def add_left(self, node):
        """
        Sets the left child of the node to the given node.
        """
        self.left = node

    def add_right(self, node):
        """Sets the right child of the node to the given node."""
        self.right = node

    def evaluate(self):
        """Evaluates the arithmetic expression represented by the BETNode object."""
        if self.value in self.CARD_VAL_DICT.keys():
            return self.CARD_VAL_DICT[self.value]
        elif self.value == '0':
            return 0
        else:
            if self.value == "+":
                left = self.left.evaluate()
                right = self.right.evaluate()
                return left + right
            if self.value == "-":
                left = self.left.evaluate()
                right = self.right.evaluate()
                return left - right
            if self.value == "*":
                left = self.left.evaluate()
                right = self.right.evaluate()
                return left * right
            if self.value == "/":
                left = self.left.evaluate()
                right = self.right.evaluate()
                if right == 0:
                    return 0
                else:
                    return left / right

    def __repr__(self):
        """Returns a string representation of the BETNode object."""
        output = ""
        if self.value in self.CARD_VAL_DICT.keys():
            output += self.value
        else:
            if self.value == "+":
                left = self.left.__repr__()
                right = self.right.__repr__()
                output += f"({left} + {right})"
            if self.value == "-":
                left = self.left.__repr__()
                right = self.right.__repr__()
                output += f"({left} - {right})"
            if self.value == "*":
                left = self.left.__repr__()
                right = self.right.__repr__()
                output += f"({left} * {right})"
            if self.value == "/":
                left = self.left.__repr__()
                right = self.right.__repr__()
                output += f"({left} / {right})"
        output = output.replace(" ", "")
        return output


def create_trees(cards):
    """Generates all possible arithmetic expressions using the given cards and operators."""
    ops = ['+', '-', '*', '/']
    valid_expressions = set()
    card_perms = permutations(cards)
    ops_perms = product(ops, repeat=3)
    card_perms = list(card_perms)
    ops_perms = list(ops_perms)
    for perm in card_perms:
        for exp in ops_perms:
            tree1 = BETNode(str(exp[2]))
            tree1.add_left(BETNode(str(exp[0])))
            tree1.left.add_left(BETNode(str(perm[0])))
            tree1.left.add_right(BETNode(str(perm[1])))
            tree1.add_right(BETNode(str(exp[1])))
            tree1.right.add_left(BETNode(str(perm[2])))
            tree1.right.add_right(BETNode(str(perm[3])))
            valid_expressions.add(tree1)

            tree2 = BETNode(str(exp[2]))
            tree2.add_left(BETNode(str(exp[1])))
            tree2.add_right(BETNode(str(perm[3])))
            tree2.left.add_left(BETNode(str(exp[0])))
            tree2.left.add_right(BETNode(str(perm[2])))
            tree2.left.left.add_left(BETNode(str(perm[0])))
            tree2.left.left.add_right(BETNode(str(perm[1])))
            valid_expressions.add(tree2)

            tree3 = BETNode(str(exp[2]))
            tree3.add_left(BETNode(str(exp[1])))
            tree3.add_right(BETNode(str(perm[3])))
            tree3.left.add_left(BETNode(str(perm[0])))
            tree3.left.add_right(BETNode(str(exp[0])))
            tree3.left.right.add_left(BETNode(str(perm[1])))
            tree3.left.right.add_right(BETNode(str(perm[2])))
            valid_expressions.add(tree3)

            tree4 = BETNode(str(exp[2]))
            tree4.add_left(BETNode(str(perm[0])))
            tree4.add_right(BETNode(str(exp[1])))
            tree4.right.add_left(BETNode(str(exp[0])))
            tree4.right.add_right(BETNode(str(perm[3])))
            tree4.right.left.add_left(BETNode(str(perm[1])))
            tree4.right.left.add_right(BETNode(str(perm[2])))
            valid_expressions.add(tree4)

            tree5 = BETNode(str(exp[2]))
            tree5.add_left(BETNode(str(perm[0])))
            tree5.add_right(BETNode(str(exp[1])))
            tree5.right.add_left(BETNode(str(perm[1])))
            tree5.right.add_right(BETNode(str(exp[0])))
            tree5.right.right.add_left(BETNode(str(perm[2])))
            tree5.right.right.add_right(BETNode(str(perm[3])))
            valid_expressions.add(tree5)
    return valid_expressions


def find_solutions():
    """Finds all possible solutions for the 24 game using the user-provided cards. Returns a set of solutions."""
    cards = input("Enter the four cards (separated by spaces): ").split()
    solution = set()
    combos = create_trees(cards)
    for x in combos:
        if x.evaluate() == 24:
            solution.add(repr(x))
    return solution

if __name__ == '__main__':
    solutions = find_solutions()
    print("Possible solutions:")
    for solution in solutions:
        print(solution)


