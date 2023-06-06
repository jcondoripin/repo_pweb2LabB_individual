from pieces import *
from picture import *
from interpreter import *

bishop = Picture(BISHOP)
king = Picture(KING)
knight = Picture(KNIGHT)
pawn = Picture(PAWN)
queen = Picture(QUEEN)
rock = Picture(ROCK)
square = Picture(SQUARE)

# draw(knight.verticalMirror())

# draw(bishop.horizontalMirror())

# draw(queen.negative())

draw(queen.join(knight))