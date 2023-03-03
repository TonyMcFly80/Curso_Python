import ApylabradosModule
from ApylabradosModule import *

ApylabradosModule.startGame()

while not ApylabradosModule.end and ApylabradosModule.bag_of_pawns.getTotalPawns() > 0:
    ApylabradosModule.showOptions()

if ApylabradosModule.bag_of_pawns.getTotalPawns() <= 0:
    print('Te has quedado sin fichas!')
    print('Fin del juego')

print(f'Enhorabuena! Has conseguido {Board.score} puntos en esta partida.')
