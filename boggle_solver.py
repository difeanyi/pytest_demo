class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = None
        self.dictionary = None
        self.solution = []
        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        """Sets the Boggle grid."""
        if isinstance(grid, list) and len(grid) > 0:
            # Check that all rows exist and have content
            if all(isinstance(row, list) and len(row) > 0 for row in grid):
                self.grid = grid
            else:
                self.grid = None
        else:
            self.grid = None

    def setDictionary(self, dictionary):
        """Sets the dictionary as a set for O(1) lookup speed."""
        if isinstance(dictionary, list):
            # Optimization: Using a set prevents the 'timeout' error
            self.dictionary = set(word.upper() for word in dictionary)
        else:
            self.dictionary = None

    def getSolution(self):
        """Finds all valid words in the grid based on the dictionary."""
        if self.grid is None or self.dictionary is None:
            return []

        found_words = set()
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        if cols == 0:
            return []

        def find_words_dfs(r, c, visited, current_word):
            # 1. Base Case: Out of bounds or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                return

            # 2. Process Current Tile
            tile = str(self.grid[r][c]).upper()
            
            # Special logic for "Qu" and "St" tiles
            if tile == "Q" or tile == "QU":
                current_word += "QU"
            elif tile == "ST":
                current_word += "ST"
            else:
                current_word += tile
            
            # 3. Check if word is valid (Length >= 3 and in dictionary)
            if len(current_word) >= 3 and current_word in self.dictionary:
                found_words.add(current_word.lower())

            # 4. Mark visited and explore neighbors
            visited[r][c] = True
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: 
                        continue
                    find_words_dfs(r + dr, c + dc, visited, current_word)
            
            # 5. Backtrack: Unmark visited for other paths
            visited[r][c] = False

        # Start DFS from every single tile
        for r in range(rows):
            for c in range(cols):
                visited_map = [[False for _ in range(cols)] for _ in range(rows)]
                find_words_dfs(r, c, visited_map, "")

        self.solution = sorted(list(found_words))
        return self.solution