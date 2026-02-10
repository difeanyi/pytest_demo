import unittest
from boggle_solver import Boggle

class TestBoggleSolver(unittest.TestCase):
    
    def test_normal_input(self):
        """1. Test normal input with valid adjacent words."""
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["ABC", "AEI", "DEF"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertIn("abc", solution)

    def test_qu_logic(self):
        """2. Test the 'Qu' special case logic."""
        # Test Case A: Grid has a single 'Q' tile, which represents 'QU'
        # Path: Q(0,0)=QU -> I(0,1) -> T(1,1) = QUIT
        grid = [["Q", "I", "X"], ["Y", "T", "Z"], ["A", "B", "C"]]
        dictionary = ["QUIT"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertIn("quit", solution)

        # Test Case B: Grid has a 'QU' tile (explicit QU tile)
        # Path: QU(0,0) -> I(0,1) -> T(1,1) = QUIT
        grid2 = [["QU", "I", "X"], ["Y", "T", "Z"], ["A", "B", "C"]]
        solver2 = Boggle(grid2, dictionary)
        solution2 = solver2.getSolution()
        self.assertIn("quit", solution2)

    def test_st_logic(self):
        """3. Test the 'St' special case logic."""
        grid = [["ST", "A", "R"], ["T", "E", "P"], ["C", "V", "B"]]
        dictionary = ["STAR", "STEP"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertIn("star", solution)
        self.assertIn("step", solution)

    def test_min_word_length(self):
        """4. Test minimum word length requirement (>= 3)."""
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["AB", "A"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_empty_grid(self):
        """5. Test empty grid edge case."""
        grid = []
        dictionary = ["APPLE"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_empty_dictionary(self):
        """6. Test empty dictionary edge case."""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_non_alphabetical_chars(self):
        """7. Test grid with non-alphabetical characters."""
        grid = [["1", "2"], ["3", "4"]]
        dictionary = ["123"]
        solver = Boggle(grid, dictionary)
        self.assertTrue(isinstance(solver.getSolution(), list))

    def test_case_insensitivity(self):
        """8. Test case insensitivity."""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["abcd"]
        solver = Boggle(grid, dictionary)
        self.assertIn("abcd", solver.getSolution())

    def test_no_valid_words(self):
        """9. Test when no valid words can be formed."""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["HELLO", "WORLD"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(len(solver.getSolution()), 0)

    def test_large_grid(self):
        """10. Test larger grid (4x4)."""
        grid = [["A", "B", "C", "D"], ["E", "F", "G", "H"], 
                ["I", "J", "K", "L"], ["M", "N", "O", "P"]]
        dictionary = ["ABCD", "AFKP"]
        solver = Boggle(grid, dictionary)
        self.assertIn("abcd", solver.getSolution())

    def test_diagonal_adjacency(self):
        """11. Test diagonal adjacency is properly recognized."""
        grid = [["C", "A", "T"], ["D", "O", "G"], ["R", "U", "N"]]
        dictionary = ["COG", "CAT"]  # CAT is horizontal, COG is diagonal
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertIn("cat", solution)
        self.assertIn("cog", solution)

    def test_path_cannot_reuse_tiles(self):
        """12. Test that a single path cannot reuse the same tile."""
        grid = [["A", "B"], ["C", "D"]]
        # "AA" would require reusing the A tile, which is not allowed
        dictionary = ["AA", "ABC"]
        solver = Boggle(grid, dictionary)
        solution = solver.getSolution()
        self.assertNotIn("aa", solution)  # Cannot reuse A
        self.assertIn("abc", solution)  # Valid path

if __name__ == '__main__':
    unittest.main()