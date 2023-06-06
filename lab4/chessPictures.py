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

# draw(knight.join(knight.replace(square).join(knight.replace(square.negative()))))


# Ejercicios propuestos (dibujar imagenes)

# Ejercicio a:

# newDraw1 = knight.join(knight.negative()) # Creamos la primera fila (caballo blanco y negro)
# newDraw2 = knight.negative().join(knight) # Creamos la segunda fila (caballo negro y blanco)

# finalDraw = newDraw1.under(newDraw2) # Colocamos uno debajo del otro
# draw(finalDraw) # Dibujamos


# Ejercicio b:

# newDraw1 = knight.join(knight.negative()) # Creamos la primera fila (caballo blanco y negro)
# newDraw2 = knight.negative().verticalMirror().join(
#     knight.verticalMirror()) # Creamos la segunda fila (caballo negro y blanco inversos)

# finalDraw = newDraw1.under(newDraw2) # Colocamos uno debajo del otro
# draw(finalDraw) # Dibujamos


# Ejercicio c:

# finalDraw = queen.horizontalRepeat(4) # Repetimos la reina 4 veces
# draw(finalDraw) # Dibujamos


# Ejercicio d:

# newDraw = square.join(square.negative()) # Creamos el par de casillas (blanco y negro)
# finalDraw = newDraw.horizontalRepeat(4) # Repetimos para 8 casillas

# draw(finalDraw) # Dibujamos


# Ejercicio e:

# newDraw = square.negative().join(square) # Creamos el par de casillas (negro y blanco)
# finalDraw = newDraw.horizontalRepeat(4) # Repetimos para 8 casillas

# draw(finalDraw) # Dibujamos


# Ejercicio f:

# newDraw1 = square.join(square.negative()) # Creamos el par de casillas (negro y blanco)
# newDraw2 = newDraw1.horizontalRepeat(4) # Repetimos para 8 casillas
# newDraw3 = square.negative().join(square) # Creamos el par de casillas (negro y blanco)
# newDraw4 = newDraw3.horizontalRepeat(4) # Repetimos para 8 casillas

# finalDraw = newDraw2.under(newDraw4).verticalRepeat(2) # Unimos las casillas y repetimos por dos

# draw(finalDraw) # Dibujamos


# Ejercicio g:

newDraw = knight.replace(square)
draw(newDraw)