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

# draw(queen.join(knight))

# draw(king.up(queen))

# draw(rock.under(king))

# draw(king.horizontalRepeat(4))

# draw(king.verticalRepeat(4))

# draw(king.join(
#     king.rotate().join(
#         king.rotate().rotate().join(
#             king.rotate().rotate().rotate().join(
#                 king.rotate().rotate().rotate().rotate()
#             )
#         )
#     )
# ))


# Ejercicios propuestos (dibujar imagenes)

# Ejercicio a:

newDraw1 = knight.join(knight.negative()) # Creamos la primera fila (caballo blanco y negro)
newDraw2 = knight.negative().join(knight) # Creamos la segunda fila (caballo negro y blanco)

finalDraw = newDraw1.under(newDraw2) # Colocamos uno debajo del otro
draw(finalDraw) # Dibujamos


# Ejercicio b:

newDraw1 = knight.join(knight.negative()) # Creamos la primera fila (caballo blanco y negro)
newDraw2 = knight.negative().horizontalMirror().join(
    knight.horizontalMirror()) # Creamos la segunda fila (caballo negro y blanco inversos)

finalDraw = newDraw1.under(newDraw2) # Colocamos uno debajo del otro
draw(finalDraw) # Dibujamos