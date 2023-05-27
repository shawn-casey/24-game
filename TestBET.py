import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        """String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    def test_evaluate_tree1(self):
        """
        Tests the evaluation of the following tree:
                        +
                       / \
                      *   5
                     / \
                    4   3
        """
        root = BETNode('+')
        root.add_left(BETNode('*'))
        root.add_right(BETNode('5'))
        root.left.add_left(BETNode('4'))
        root.left.add_right(BETNode('3'))
        self.assertEqual(root.evaluate(), 17)

    def test_evaluate_tree2(self):
        """
        Tests the evaluation of the following tree:
                        -
                       / \
                      *   5
                     / \
                    4   3
        """
        root = BETNode('-')
        root.add_left(BETNode('*'))
        root.add_right(BETNode('5'))
        root.left.add_left(BETNode('4'))
        root.left.add_right(BETNode('3'))
        self.assertEqual(root.evaluate(), 7)

class TestCreateTrees(unittest.TestCase):
    def setUp(self):
        """Initializes two hands of cards, one with face cards and one with number cards."""
        self.hand1 = ["A", "K", "Q", "J"]
        self.hand2 = [9, 8, 7, 6]

    def test_hand1(self):
        """Tests if the first hand contains the expected cards."""
        expected = ["A", "K", "Q", "J"]
        actual = self.hand1
        self.assertEqual(expected, actual)

    def test_hand2(self):
        """Tests if the second hand contains the expected cards."""
        expected = [9, 8, 7, 6]
        actual = self.hand2
        self.assertEqual(expected, actual)


class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        """Tests if a hand with only one type of card has no solutions."""
        def mock_input(prompt):
            return '1 1 1 1'
        find_solutions.input = mock_input
        solutions = find_solutions()
        self.assertEqual(len(solutions), 0)

    def test_A23Q(self):
        """Tests if a hand with four different cards has the expected number of solutions."""
        def mock_input(prompt):
            return 'A 2 3 Q'
        find_solutions.input = mock_input
        solutions = find_solutions()
        self.assertEqual(len(solutions), 33)


if __name__ == '__main__':
    unittest.main()