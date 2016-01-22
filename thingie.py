EMPTYCHAR = 0

# If you're reading this code, burn it now.
# For your protection, we have provided a safety pig:
#                           _
#  _._ _..._ .-',     _.._(`))
# '-. `     '  /-._.-'    ',/
#    )         \            '.
#   / _    _    |             \
#  |  a    a    /              |
#  \   .-.                     ;
#   '-('' ).-'       ,'       ;
#      '-;           |      .'
#         \           \    /
#         | 7  .__  _.-\   \
#         | |  |  ``/  /`  /
#    jgs /,_|  |   /,_/   /
#           /,_/      '`-'
# Love,
#       Maia and Rose

class SmallBoard:
    def __init__(self, n=3):
        self.squares = [[EMPTYCHAR for _ in range(n)] for _ in range(n)]
        self.winner = None
        self.size = n

    ### Board info funcs
    def empty_squares(self):
        return [(i,j) for i in range(self.size) for j in range(self.size) if self.squares[i][j] == EMPTYCHAR]

    def rows(self):
        return self.squares

    def cols(self):
        return [[self.squares[i][j] for i in range(self.size)] for j in range(self.size)]

    def diags(self):
        return [[self.squares[i][i] for i in range(self.size)],
                [self.squares[i][self.size - i - 1] for i in range(self.size)]]

    def check_if_won(self):
        """Check if board is won. DOOOOOCCCCSTRIIIINNNNNGGGG."""
        all_triplets = self.rows() + self.cols() + self.diags()
        for triplet in all_triplets:
            if len(set(triplet)) == 1 and triplet[0] != EMPTYCHAR:
                # A WINNAR IS YOU
                return True
        return False

    def move(self, token, row, col):
        if not (0 <= row <= self.size and 0 <= col <= self.size):
            # TODO: custom exception? Maia is awesome.
            raise Exception("Invalid position")

        # NOTE: this will have to change if we ever go back to empty squares as 'none'
        if self.squares[row][col] != EMPTYCHAR:
            raise Exception("Square is taken, illegal move")

        self.squares[row][col] = token

    def __str__(self):
        strings = []
        for row in self.squares:
            strings.append("  ".join([str(n) for n in row]))

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