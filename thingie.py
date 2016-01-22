class SmallBoard:
    def __init__(self, n=3):
        self.squares = [[0 for _ in range(n)] for _ in range(n)]
        self.winner = None
        self.size = n

    def check_if_won(self):
        # can check if just a particular move wins?
        pass

    def move(self, token, row, col):
        if not (0 <= row <= self.size and 0 <= col <= self.size):
            # TODO: custom exception? Maia is awesome.
            raise Exception("Invalid position")

        # NOTE: this will have to change if we ever go back to empty squares as 'none'
        if self.squares[row][col]:
            raise Exception("Square is taken, illegal move")

        self.squares[row][col] = token

    def get_empty_squares(self):
        pass

    def __str__(self):
        strings = []
        for row in self.squares:
            strings.append("  ".join([str(i) for i in row]))

        return "\n".join(strings)

class LargeBoard:
    def __init__(self):
        pass

class Player:
    # get moves
    def __init__(self):
        pass

class Human(Player):
    pass

class Computer(Player):
    pass

class Game:
    def __init__(self):
        pass