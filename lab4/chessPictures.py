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


# Ejercicio g: Tablero completo

# Patron de colocación
patron1 = [rock, knight, bishop]
patron2 = [queen, king]

filaPiezas1 = patron1 + patron2 + patron1[::-1]
filaPiezas2 = [pawn] * 8

casillas1 = square.join(square.negative()) # Creamos el par de casillas (negro y blanco)
casillas2 = casillas1.horizontalRepeat(4) # Repetimos para 8 casillas
casillas3 = square.negative().join(square) # Creamos el par de casillas (negro y blanco)
casillas4 = casillas3.horizontalRepeat(4) # Repetimos para 8 casillas

casillas = casillas2.under(casillas4)

fila1 = filaPiezas1[0].negative()
for pieza in filaPiezas1[1:-1]:
    fila1 = fila1.join(pieza.negative())
fila1 = fila1.join(filaPiezas1[-1].negative())

fila2 = filaPiezas2[0].negative()
for pieza in filaPiezas2[1:-1]:
    fila2 = fila2.join(pieza.negative())
fila2 = fila2.join(filaPiezas2[-1].negative())

filasCasillas1 = fila1.under(fila2).replace(casillas)

filasCasillas2 = fila2.negative().under(fila1.negative()).replace(casillas)

tablero = filasCasillas1.under(casillas.verticalRepeat(2).under(filasCasillas2))
draw(tablero)
    





