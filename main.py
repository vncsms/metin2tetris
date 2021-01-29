from tetris import Tetris
from piece import Piece
from copy import deepcopy
import random
random.seed(111)

def get_new_piece():
    return Piece(random.randint(1,6))

def search_tree(tetris):

    total = 0

    while not tetris.verify_end():

        piece = get_new_piece()
        ## print(piece)
        total += 1
        possibilites = tetris.find_possibles(piece)
        ## print(possibilites)
        pices_count = 0

        for i in range(1,7):
            if i != piece.piece_type:
                possis = tetris.find_possibles(Piece(i))
                if len(possis):
                    pices_count += 1

        if piece.piece_type == 1 and pices_count != 0:
            possibilites = [i for i in possibilites if tetris.verify_isolated(i[0], i[1])]

        if len(possibilites):

            a = tetris.choose_better(piece, possibilites)

            tetris.insert_piece(a[0], a[1], piece)
            

    return total

def main():

    total = 0
    points_1 = 0
    points_2 = 0
    points_3 = 0

    length = 1000

    for i in range(0, length):
        tetris = Tetris()
        t = search_tree(tetris)

        if t <= 10:
            points_3 += 1
        elif t >= 11 and t <= 24:
            points_2 += 1
        else:
            points_1 += 1

        total += t

    print("Total pieces: ", total)
    print("Average: ", total/length)
    print("3 Points: ", points_3)
    print("2 Points: ", points_2)
    print("1 Points: ", points_1)

main()