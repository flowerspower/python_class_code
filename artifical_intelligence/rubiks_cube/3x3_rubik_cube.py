# -*- coding: cp1252 -*-
import sys  # In order to make the output pause for a couple of seconds
from vpython import *
import random

fps = 24  # Regulates the frame per second parameter
number = 0  # For counting the overall number of movements undertaken
faces = {'R': (color.green, (1, 0, 0)),
         'L': (color.blue, (-1, 0, 0)),
         'U': (color.yellow, (0, 1, 0)),
         'D': (color.white, (0, -1, 0)),
         'B': (color.orange, (0, 0, -1)),
         'F': (color.red, (0, 0, 1))}

# In this step, we color the Rubik's cube face by face and hut by hut
paintings = []
for color_face, axis in faces.values():
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            # We proceed by the hut on the top then we rotate the Rubik's cube
            painting = box(color=color_face, pos=vector(x, y, 1.5), length=0.98, height=0.98, width=0.05)
            angle = dot(vector(0, 0, 1), axis)
            pivot = (cross((0, 0, 1), axis) if angle == 0 else (1, 0, 0))
            painting.rotate(angle=acos(angle), axis=pivot, origin=(0, 0, 0))
            paintings.append(painting)


# Function that diplays the Rubik's cube's rotations in 3D
def threeD_rotation(key):
    if key[0] in faces:
        color_face, axis = faces[key[0]]
        angle = ((pi / 2) if len(key) > 1 else -pi / 2)
        for r in arange(0, angle, angle / fps):
            rate(fps)
            for painting in paintings:
                if dot(painting.pos, axis) > 0.5:
                    painting.rotate(angle=angle / fps, axis=axis, origin=(0, 0, 0))
    elif key[0] == 'E':
        axis = (0, 0.5, 0)
        angle = ((pi / 2) if len(key) > 1 else -pi / 2)
        for r in arange(0, angle, angle / fps):
            rate(fps)
            for painting in paintings:
                painting.rotate(angle=angle / fps, axis=axis, origin=(0, 0, 0))


# The kernels
r = 'g'  # Right/Green
l = 'b'  # Left /Blue
d = 'w'  # Down/White
u = 'y'  # Up/Yellow
f = 'r'  # Face/Red
b = 'o'  # Back/Orange

# Taking care of the edges and corners; the names of variables had been made intuitive (position of the hut in the Rubik's cube)
# The general format is: {'face' : 'color of the hut'}
df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''}
dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''}
db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''}
dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'}
uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''}
ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''}
ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''}
ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'}
fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}

ufr = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}
dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}


# Function that controls the movements
def move(face, show=1):
    global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
    global number
    number += 1
    if show == 1:
        sys.stdout.write(face + ", ")  # We display the movement followed by a comma

    # We list all the differents possibilities (if the movement shows R, R' etc)

    # <> <Smile> <> #
    if face == "R":
        ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr['f'], \
        dfr['r'], = \
            dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr[
                'd'], dbr['r']

        ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r'], fr['f'], fr['r'], = \
            fr['f'], fr['r'], ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r']  # Edges and corners
        threeD_rotation("R")

    # <> <Smile> <> #
    if face == "R'":
        dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr['d'], \
        dbr['r'], = \
            ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr[
                'f'], dfr['r']

        ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r'], br['b'], br['r'], = \
            br['b'], br['r'], ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r']
        threeD_rotation("R'")

    # <> <Smile> <> #
    if face == "U":
        ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], \
        ufl['l'], = \
            ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr[
                'r'], ufr['f']

        ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'], = \
            ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']
        threeD_rotation("U")

    # <> <Smile> <> #
    if face == "U'":
        ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], \
        ufr['f'], = \
            ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl[
                'f'], ufl['l']

        ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'], = \
            uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'], ur['u'], ur['r']
        threeD_rotation("U'")

    # <> <Smile> <> #
    if face == "D":
        dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], \
        dfr['f'], = \
            dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl[
                'f'], dfl['l']

        dr['d'], dr['r'], df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'], = \
            df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'], dr['d'], dr['r']
        threeD_rotation("D")

    # <> <Smile> <> #
    if face == "D'":
        dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], \
        dfl['l'], = \
            dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr[
                'r'], dfr['f']

        df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], = \
            dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']
        threeD_rotation("D'")

    # <> <Smile> <> #
    if face == "L'":
        ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], \
        dfl['l'], = \
            dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl[
                'd'], dbl['l']

        ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l'], fl['f'], fl['l'], = \
            fl['f'], fl['l'], ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l']  # Aletes
        threeD_rotation("L'")

    # <> <Smile> <> #
    if face == "L":
        dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl['d'], \
        dbl['l'], = \
            ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl[
                'f'], dfl['l']

        ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l'], bl['b'], bl['l'], = \
            bl['b'], bl['l'], ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l']
        threeD_rotation("L")

    # <> <Smile> <> #
    if face == "F":
        ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl['f'], \
        ufl['l'], = \
            ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl[
                'f'], dfl['d']

        uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], = \
            fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f']
        threeD_rotation("F")

    # <> <Smile> <> #
    if face == "F'":
        ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl['f'], \
        dfl['d'], = \
            ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl[
                'f'], ufl['l']

        fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f'], = \
            uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f']
        threeD_rotation("F'")

    # <> <Smile> <> #
    if face == "B'":
        ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl['b'], \
        ubl['l'], = \
            ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl[
                'b'], dbl['d']

        ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], = \
            bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b']
        threeD_rotation("B'")

    # <> <Smile> <> #
    if face == "B":
        ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl['b'], \
        dbl['d'], = \
            ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl[
                'b'], ubl['l']

        bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b'], = \
            ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b']
        threeD_rotation("B")


def mixte(nbrDeMoves=25, show=1):
    list_of_movements = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]

    i = 0
    for i in range(nbrDeMoves):
        aleatoire = random.randint(0, 11)
        move(list_of_movements[aleatoire], 0)
        if show == 1:
            sys.stdout.write(str(list_of_movements[aleatoire]).upper() + " ")
    if show == 1:
        print("\nThe Rubik's cube has been mixed !")


def display_RC():
    print("\n\t" + ubl['u'] + ub['u'] + ubr['u'] + "\n\t" + \
          ul['u'] + u + ur['u'] + "\n\t" + \
          ufl['u'] + uf['u'] + ufr['u'] + "\n" + \
 \
          ubl['l'] + ul['l'] + ufl['l'] + " " + ufl['f'] + uf['f'] + ufr['f'] + " " + ufr['r'] + ur['r'] + ubr[
              'r'] + " " + ubr['b'] + ub['b'] + ubl['b'] + "\n" + \
          bl['l'] + l + fl['l'] + " " + fl['f'] + f + fr['f'] + " " + fr['r'] + r + br['r'] + " " + br['b'] + b + bl[
              'b'] + " " + "\n" + \
          dbl['l'] + dl['l'] + dfl['l'] + " " + dfl['f'] + df['f'] + dfr['f'] + " " + dfr['r'] + dr['r'] + dbr[
              'r'] + " " + dbr['b'] + db['b'] + dbl['b'] + "\n\t" + \
 \
          dfl['d'] + df['d'] + dfr['d'] + "\n\t" + dl['d'] + d + dr['d'] + "\n\t" + dbl['d'] + db['d'] + dbr[
              'd'] + "\n")

    print("<><><><><><><><><><><><><><><><><>")


def Right_Left_RC(show=1):  # Right to left turn
    global d, u, f, b, r, l

    # U
    ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl[
        'l'], = \
        ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], \
        ufr['f']

    ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'], = \
        ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']

    # D'
    dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl[
        'l'], = \
        dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], \
        dfr['f']

    df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], = \
        dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']

    # E'
    fl['f'], fl['l'], fr['f'], fr['r'], br['b'], br['r'], bl['b'], bl['l'] = \
        fr['r'], fr['f'], br['r'], br['b'], bl['l'], bl['b'], fl['l'], fl['f']

    f, r, b, l = \
        r, b, l, f

    threeD_rotation("E")

    if show == 1:
        print("The Rubik's cube has been turned.")


def resetCube():
    # Centers
    d = 'w'
    u = 'y'
    f = 'r'
    b = 'o'
    r = 'g'
    l = 'b'

    # Edges and corners; same format as previously {'face/direction' : 'color'}
    uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''}
    ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''}
    ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''}
    ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'}
    df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''}
    dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''}
    db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''}
    dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'}
    fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
    fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
    br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
    bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}

    ufr = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
    ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
    ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
    ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}
    dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
    dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
    dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
    dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}


def solving_white_cross(show=1):
    if show == 1:
        print("\nBuilding the white cross :\n")
    global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
    liste = ['r', 'g', 'o', 'b']

    for i in liste:
        if dr['d'] == 'w' and dr['r'] == i:
            move("R", show)
            move("R", show)
            move("U", show)
            move("F", show)
            move("F", show)

        elif db['d'] == 'w' and db['b'] == i:
            move("B", show)
            move("B", show)
            move("U", show)
            move("U", show)
            move("F", show)
            move("F", show)

        elif dl['d'] == 'w' and dl['l'] == i:
            move("L", show)
            move("L", show)
            move("U'", show)
            move("F", show)
            move("F", show)

        elif fr['f'] == 'w' and fr['r'] == i:
            move("R", show)
            move("U", show)
            move("R'", show)
            move("F", show)
            move("F", show)

        elif fl['f'] == 'w' and fl['l'] == i:
            move("L'", show)
            move("U'", show)
            move("L", show)
            move("F", show)
            move("F", show)

        elif br['b'] == 'w' and br['r'] == i:
            move("R'", show)
            move("U", show)
            move("R", show)
            move("F", show)
            move("F", show)

        elif bl['b'] == 'w' and bl['l'] == i:
            move("L", show)
            move("U'", show)
            move("L'", show)
            move("F", show)
            move("F", show)

        elif uf['u'] == 'w' and uf['f'] == i:
            move("F", show)
            move("F", show)

        elif ur['u'] == 'w' and ur['r'] == i:
            move("U", show)
            move("F", show)
            move("F", show)

        elif ul['u'] == 'w' and ul['l'] == i:
            move("U'", show)
            move("F", show)
            move("F", show)

        elif ub['u'] == 'w' and ub['b'] == i:
            move("U", show)
            move("U", show)
            move("F", show)
            move("F", show)

        elif dr['d'] == i and dr['r'] == 'w':
            move("R", show)
            move("F", show)

        elif db['d'] == i and db['b'] == 'w':
            move("B", show)
            move("D", show)
            move("R", show)
            move("D'", show)

        elif dl['d'] == i and dl['l'] == 'w':
            move("L'", show)
            move("F'", show)

        elif fr['f'] == i and fr['r'] == 'w':
            move("F", show)

        elif fl['f'] == i and fl['l'] == 'w':
            move("F'", show)

        elif br['b'] == i and br['r'] == 'w':
            move("B", show)
            move("U", show)
            move("U", show)
            move("B'", show)
            move("F", show)
            move("F", show)

        elif bl['b'] == i and bl['l'] == 'w':
            move("B'", show)
            move("U", show)
            move("U", show)
            move("B", show)
            move("F", show)
            move("F", show)

        elif uf['u'] == i and uf['f'] == 'w':
            move("U'", show)
            move("R'", show)
            move("F", show)
            move("R", show)

        elif ur['u'] == i and ur['r'] == 'w':
            move("R'", show)
            move("F", show)
            move("R", show)

        elif ul['u'] == i and ul['l'] == 'w':
            move("L", show)
            move("F'", show)
            move("L'", show)

        elif ub['u'] == i and ub['b'] == 'w':
            move("U", show)
            move("R'", show)
            move("F", show)
            move("R", show)

        elif df['d'] == i and df['f'] == 'w':
            move("F'", show)
            move("D", show)
            move("R'", show)
            move("D'", show)
        Right_Left_RC(show)


def solving_white_corners(show=1):
    if show == 1:
        print("\nPlacing the white corners :\n")
    global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
    liste = ["wrg", "wgo", "wob", "wbr"]

    for j in liste:

        if ufl['u'] in j and ufl['f'] in j and ufl['l'] in j:
            move("U'", show)

        elif ubl['u'] in j and ubl['b'] in j and ubl['l'] in j:
            move("U'", show)
            move("U'", show)

        elif ubr['u'] in j and ubr['b'] in j and ubr['r'] in j:
            move("U", show)

        elif dfl['d'] in j and dfl['f'] in j and dfl['l'] in j:
            move("L'", show)
            move("U'", show)
            move("L", show)

        elif dbl['d'] in j and dbl['b'] in j and dbl['l'] in j:
            move("L", show)
            move("U", show)
            move("U", show)
            move("L'", show)

        elif dbr['d'] in j and dbr['b'] in j and dbr['r'] in j:
            move("R'", show)
            move("U", show)
            move("R", show)
            move("U", show)

        if dfr['r'] == 'w' and dfr['d'] in j and dfr['f'] in j:
            move("R", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("R", show)
            move("U", show)
            move("R'", show)

        if dfr['f'] == 'w' and dfr['d'] in j and dfr['r'] in j:
            move("F'", show)
            move("U'", show)
            move("F", show)
            move("U", show)
            move("F'", show)
            move("U'", show)
            move("F", show)

        if ufr['u'] == 'w' and ufr['f'] in j and ufr['r'] in j:
            move("R", show)
            move("U", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("R", show)
            move("U", show)
            move("R'", show)

        if ufr['f'] == 'w' and ufr['u'] in j and ufr['r'] in j:
            move("U", show)
            move("R", show)
            move("U'", show)
            move("R'", show)

        if ufr['r'] == 'w' and ufr['u'] in j and ufr['f'] in j:
            move("R", show)
            move("U", show)
            move("R'", show)

        Right_Left_RC(show)


def ended():
    global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl

    if d == 'w' and \
            u == 'y' and \
            f == 'r' and \
            b == 'o' and \
            r == 'g' and \
            l == 'b' and \
            uf == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
            ur == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
            ub == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
            ul == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
            df == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
            dr == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
            db == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
            dl == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
            fr == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
            fl == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
            br == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
            bl == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
            ufr == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
            ufl == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
            ubr == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
            ubl == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
            dfr == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
            dfl == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
            dbr == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
            dbl == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}:

        return 1
    else:
        return 0


def solving_second_stage(show=1):  # Resolving the second stage

    if show == 1:
        print("\nBuilding the second stage :\n")
    global uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl
    liste = ['rg', 'go', 'ob', 'br']  # Colors of an edge and two cornes x 2 [juxtaposition]

    for i in liste:

        if fl['f'] in i and fl['l'] in i:
            move("F", show)
            move("U", show)
            move("F'", show)
            move("U'", show)
            move("L'", show)
            move("U'", show)
            move("L", show)

        if br['b'] in i and br['r'] in i:
            Right_Left_RC(show)
            Right_Left_RC(show)
            move("F", show)
            move("U", show)
            move("F'", show)
            move("U'", show)
            move("L'", show)
            move("U'", show)
            move("L", show)
            Right_Left_RC(show)
            Right_Left_RC(show)

        if bl['b'] in i and bl['l'] in i:
            Right_Left_RC(show)
            Right_Left_RC(show)
            Right_Left_RC(show)
            move("F", show)
            move("U", show)
            move("F'", show)
            move("U'", show)
            move("L'", show)
            move("U'", show)
            move("L", show)
            Right_Left_RC(show)

        if fr['r'] is i[0] and fr['f'] in i:
            move("R", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("U'", show)
            move("R", show)
            move("U'", show)
            move("U'", show)
            move("R'", show)
            move("U", show)
            move("F'", show)
            move("U'", show)
            move("F", show)

        if uf['f'] is i[0] and uf['u'] in i:
            move("U", show)
            move("R", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("F'", show)
            move("U'", show)
            move("F", show)

        if uf['u'] is i[0] and uf['f'] in i:
            move("U'", show)
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U", show)
            move("R", show)
            move("U", show)
            move("R", show)

        if ur['u'] is i[0] and ur['r'] in i:
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U", show)
            move("R", show)
            move("U", show)
            move("R", show)

        if ur['r'] is i[0] and ur['u'] in i:
            move("U", show)
            move("U", show)
            move("R", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("F'", show)
            move("U'", show)
            move("F", show)

        if ub['b'] is i[0] and ub['u'] in i:
            move("U'", show)
            move("R", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("F'", show)
            move("U'", show)
            move("F", show)

        if ub['u'] is i[0] and ub['b'] in i:
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U", show)
            move("R", show)
            move("U", show)
            move("R", show)

        if ul['l'] is i[0] and ul['u'] in i:
            move("R", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("F'", show)
            move("U'", show)
            move("F", show)

        if ul['u'] is i[0] and ul['l'] in i:
            move("U", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U'", show)
            move("R'", show)
            move("U", show)
            move("R", show)
            move("U", show)
            move("R", show)

        if fr['f'] is i[0] and fr['r'] in i and show == 1:
            print("The edge and its corners has been built.")

        Right_Left_RC(show)


def solving_yellow_cross(show=1):
    if show == 1:
        print("\nBuilding the yellow cross :\n")

    global uf, ur, ub, ul

    if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] != 'y':  # If the point is yellow then :
        move("R'", show)
        move("U'", show)
        move("F'", show)
        move("U", show)
        move("F", show)
        move("R", show)

    if uf['u'] != 'y' and ub['u'] != 'y' and ur['u'] == 'y' and ul['u'] == 'y':  # If the yellow line is finished :
        move("R'", show)
        move("U'", show)
        move("F'", show)
        move("U", show)
        move("F", show)
        move("R", show)

    if ur['u'] != 'y' and ul['u'] != 'y' and uf['u'] == 'y' and ub['u'] == 'y':  # Otherwise :
        move("U", show)  # Simple rotation of the top face to adjust the yellow line
        move("R'", show)
        move("U'", show)
        move("F'", show)
        move("U", show)
        move("F", show)
        move("R", show)

    if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] == 'y' and ul['u'] == 'y':  # If the yellow "L" shape is finished :
        move("R'", show)
        move("U'", show)
        move("F'", show)
        move("U", show)
        move("F", show)
        move("R", show)

    if uf['u'] != 'y' and ur['u'] == 'y' and ub['u'] == 'y' and ul['u'] != 'y':  # Otherwise :
        move("U'", show)
        move("R'", show)
        move("U'", show)
        move("F'", show)
        move("U", show)
        move("F", show)
        move("R", show)

    if uf['u'] == 'y' and ur['u'] == 'y' and ub['u'] != 'y' and ul['u'] != 'y':
        move("U", show)
        move("U", show)
        move("R'", show)
        move("U'", show)
        move("F'", show)
        move("U", show)
        move("F", show)
        move("R", show)

    if uf['u'] == 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] == 'y':
        move("U", show)
        move("R'", show)
        move("U'", show)
        move("F'", show)
        move("U", show)
        move("F", show)
        move("R", show)

    # The cross is built !

    # Adjusting the colors
    loop = 1  # Are the colors in their position ? The loop variable is used to answer the question
    while loop:
        if uf['f'] == 'r' and ur['r'] == 'g':
            move("U", show)
            move("U", show)

        elif ul['l'] == 'r' and uf['f'] == 'g':
            move("U", show)

        elif ur['r'] == 'r' and ub['b'] == 'g':
            move("U'", show)

        if uf['f'] == 'g' and ur['r'] == 'o':
            move("U", show)
            move("U", show)

        elif ul['l'] == 'g' and uf['f'] == 'o':
            move("U", show)

        elif ur['r'] == 'g' and ub['b'] == 'o':
            move("U'", show)

        if uf['f'] == 'o' and ur['r'] == 'b':
            move("U", show)
            move("U", show)

        elif ul['l'] == 'o' and uf['f'] == 'b':
            move("U", show)

        elif ur['r'] == 'o' and ub['b'] == 'b':
            move("U'", show)

        if uf['f'] == 'b' and ur['r'] == 'r':
            move("U", show)
            move("U", show)

        elif ul['l'] == 'b' and uf['f'] == 'r':
            move("U", show)

        elif ur['r'] == 'b' and ub['b'] == 'r':
            move("U'", show)

        # Technical algorithm
        move("U", show)
        move("R", show)
        move("U", show)
        move("R'", show)
        move("U", show)
        move("R", show)
        move("U", show)
        move("U", show)
        move("R'", show)

        # Testing the Rubik's cube to know if the colors can be placed only by "U" moves
        if ul['l'] == 'r' and uf['f'] == 'g' and ur['r'] == 'o' and ub['b'] == 'b':
            move("U'", show)
        if ul['l'] == 'o' and uf['f'] == 'b' and ur['r'] == 'r' and ub['b'] == 'g':
            move("U", show)
        if ul['l'] == 'g' and uf['f'] == 'o' and ur['r'] == 'b' and ub['b'] == 'r':
            move("U", show)
            move("U", show)
        if ul['l'] == 'b' and uf['f'] == 'r' and ur['r'] == 'g' and ub['b'] == 'o':
            loop = 0  # If the cross/colors are correctly placed, we exit the loop


def solving_final(show=1):
    if show == 1:
        print("\nPlacing the yellow corners :\n")

    while 1:

        if ('r' in ufr.values() and 'g' in ufr.values()) and \
                ('b' in ufl.values() and 'r' in ufl.values()) and \
                ('g' in ubr.values() and 'o' in ubr.values()) and \
                ('b' in ubl.values() and 'o' in ubl.values()):
            break

        if 'g' in ubr.values() and 'o' in ubr.values():  # If green/orange are contained in the values of ubr (up-back-right) then :
            move("U", show)
            move("U", show)
            move("R", show)
            move("U'", show)
            move("L'", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("L", show)
            move("U'", show)

        elif 'r' in ufr.values() and 'g' in ufr.values():
            move("U", show)
            move("R", show)
            move("U'", show)
            move("L'", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("L", show)

        elif 'b' in ubl.values() and 'o' in ubl.values():
            move("U'", show)
            move("R", show)
            move("U'", show)
            move("L'", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("L", show)
            move("U", show)
            move("U", show)

        elif 'b' in ufl.values() and 'r' in ufl.values():
            move("R", show)
            move("U'", show)
            move("L'", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("L", show)
            move("U", show)

        else:
            move("U", show)
            move("R", show)
            move("U'", show)
            move("L'", show)
            move("U", show)
            move("R'", show)
            move("U'", show)
            move("L", show)

    while 1:
        if ufr['u'] == 'y':  # If the yellow color of the Rubik's cube is on top
            if ended():  # If the RC is resolved
                break

            move("U'", show)  # Moving to the next hut

        if ufr['r'] == 'y':  # If the yellow color of the hut is on the right of the RC
            move("R'", show)
            move("D'", show)
            move("R", show)
            move("D", show)

            move("R'", show)
            move("D'", show)
            move("R", show)
            move("D", show)

        if ufr['f'] == 'y':  # If it's in the front (face):
            move("R'", show)
            move("D'", show)
            move("R", show)
            move("D", show)

            move("R'", show)
            move("D'", show)
            move("R", show)
            move("D", show)

            move("R'", show)
            move("D'", show)
            move("R", show)
            move("D", show)

            move("R'", show)
            move("D'", show)
            move("R", show)
            move("D", show)


print("Mixture of the cube :\n")
mixte()
display_RC()
print("The mixture has ended !\n")
sleep(3)

##### Solving #####

if ended():  # If the RC is solved
    print("Ended in " + str(number) + " moves !")
    quit()

solving_white_cross()  # Solving the white cross

if ended():
    print("Ended in " + str(number) + " moves !")
    quit()

solving_white_corners()  # Solving white corners

display_RC()

if ended():
    print("Ended in " + str(number) + " moves !")
    quit()

solving_second_stage()

display_RC()

if ended():
    print("Ended in " + str(number) + " moves !")
    quit()

solving_yellow_cross()

display_RC()

if ended():
    print("Ended in " + str(number) + " moves !")
    quit()

solving_final()  # Solving the corner of the yellow face

display_RC()

if ended():
    print("Ended in " + str(number) + " moves !")
    quit()

display_RC()  # we display the RC in case of some unexpected error
