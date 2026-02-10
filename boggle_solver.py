class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = None
        self.dictionary = None
        self.solution = []
        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        if isinstance(grid, list) and len(grid) > 0:
            self.grid = grid
        else:
            self.grid = None

    def setDictionary(self, dictionary):
        if isinstance(dictionary, list):
            self.dictionary = [word.upper() for word in dictionary]
        else:
            self.dictionary = None

    def getSolution(self):
        if self.grid is None or self.dictionary is None:
            return []

        found_words = set()
        rows = len(self.grid)
        cols = len(self.grid[0])

        def find_words_dfs(r, c, visited, current_word):
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                return

            tile = self.grid[r][c].upper()
            current_word += tile
            
            if len(current_word) >= 3 and current_word in self.dictionary:
                found_words.add(current_word.lower())

            visited[r][c] = True
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue
                    find_words_dfs(r + dr, c + dc, visited, current_word)
            visited[r][c] = False

        for r in range(rows):
            for c in range(cols):
                visited_map = [[False for _ in range(cols)] for _ in range(rows)]
                find_words_dfs(r, c, visited_map, "")

        self.solution = sorted(list(found_words))
        return self.solution

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()