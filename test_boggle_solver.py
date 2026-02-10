import unittest
from boggle_solver import Boggle

class TestBoggleSolver(unittest.TestCase):
    
    def test_normal_input(self):
        """1. Test a standard 3x3 grid with common words."""
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["ABC", "AEI", "DEF"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertIn("abc", solution)
        self.assertIn("aei", solution)

    def test_qu_logic(self):
        """2. Test the 'Qu' special case logic."""
        # Ensure the tiles are individual letters or "QU" depending on your solver
        grid = [["Q", "A", "R"], ["T", "Z", "X"], ["C", "V", "B"]]
        dictionary = ["QUARTZ"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertIn("quartz", solution)

    def test_min_word_length(self):
        """3. Ensure words < 3 characters are not returned."""
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["AB", "A"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_empty_grid(self):
        """4. Edge Case: Empty grid handling."""
        grid = []
        dictionary = ["APPLE"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_empty_dictionary(self):
        """5. Edge Case: Empty dictionary handling."""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_non_alphabetical_chars(self):
        """6. Test grid with numbers (should handle safely)."""
        grid = [["1", "2"], ["3", "4"]]
        dictionary = ["123"]
        solver = Boggle(grid, dictionary)
        self.assertTrue(isinstance(solver.getSolution(), list))

    def test_case_insensitivity(self):
        """7. Match lowercase dictionary words to uppercase grid tiles."""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["abcd"]
        solver = Boggle(grid, dictionary)
        # Match the lowercase output of your solver
        self.assertIn("abcd", solver.getSolution())

    def test_no_valid_words(self):
        """8. Valid grid/dictionary but no possible paths."""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["HELLO", "WORLD"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_large_grid(self):
        """9. Test logic on a standard 4x4 grid to avoid Codio timeout."""
        grid = [["A", "B", "C", "D"],
                ["E", "F", "G", "H"],
                ["I", "J", "K", "L"],
                ["M", "N", "O", "P"]]
        dictionary = ["ABCD", "AFKP", "DGJK"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertIn("abcd", solution)

    def test_multiple_occurrences(self):
        """10. Ensure same word isn't duplicated in solution list."""
        grid = [["A", "B"], ["B", "A"]]
        dictionary = ["ABA"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        # Match the lowercase output of your solver
        self.assertEqual(solution.count("aba"), 1)

if __name__ == '__main__':
    unittest.main()