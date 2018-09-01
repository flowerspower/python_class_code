"""
Milestones:
1. Draw a 3D Rubik's cube consisting of 3x3x6 thin boxes with the same color on each of the 6 faces
2. Write a function that performs one specified rotation without animation
3. Write a function that randomly rotates the rubik's cube a bunch of times
4. Write an autosolver that emits a list of rotation function calls that solves the puzzle
5. Hook up everything
6. Add animation effects to rotation and slow down the rotation operations
"""

from vpython import *
import random

GAP = 0.03
THICKNESS = 0.0005
INNER_COLOR = color.black


class RubiksCube:
    def __init__(self):
        self.rotating = False
        orange_faces = []
        black_faces_behind_orange_faces1 = []
        black_faces_behind_orange_faces2 = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                mybox = box(pos=vector(x, y, 1.5 - GAP/2),
                            length=1 - GAP, height=1 - GAP, width=THICKNESS,
                            color=color.orange)
                orange_faces.append(mybox)
                mybox = box(pos=vector(x, y, 0.5+GAP/2), length=1 - GAP, height=1 - GAP, width=THICKNESS,
                            color=INNER_COLOR)
                black_faces_behind_orange_faces1.append(mybox)
                mybox = box(pos=vector(x, y, 0.5-GAP/2), length=1 - GAP, height=1 - GAP, width=THICKNESS,
                            color=INNER_COLOR)
                black_faces_behind_orange_faces2.append(mybox)

        white_faces = []
        black_faces_behind_white_faces1 = []
        black_faces_behind_white_faces2 = []
        for x in range(-1, 2):
            for z in range(-1, 2):
                mybox = box(pos=vector(x, 1.5 - GAP/2, z), length=1 - GAP, height=THICKNESS, width=1 - GAP,
                            color=color.white)
                white_faces.append(mybox)
                mybox = box(pos=vector(x, 0.5+GAP/2, z), length=1 - GAP, height=THICKNESS, width=1 - GAP,
                            color=INNER_COLOR)
                black_faces_behind_white_faces1.append(mybox)
                mybox = box(pos=vector(x, 0.5-GAP/2, z), length=1 - GAP, height=THICKNESS, width=1 - GAP,
                            color=INNER_COLOR)
                black_faces_behind_white_faces2.append(mybox)

        green_faces = []
        black_faces_behind_green_faces1 = []
        black_faces_behind_green_faces2 = []
        for y in range(-1, 2):
            for z in range(-1, 2):
                mybox = box(pos=vector(1.5 - GAP/2, y, z), length=THICKNESS, height=1 - GAP, width=1 - GAP,
                            color=color.green)
                green_faces.append(mybox)
                mybox = box(pos=vector(0.5 + GAP/2, y, z), length=THICKNESS, height=1 - GAP, width=1 - GAP,
                            color=INNER_COLOR)
                black_faces_behind_green_faces1.append(mybox)
                mybox = box(pos=vector(0.5 - GAP/2, y, z), length=THICKNESS, height=1 - GAP, width=1 - GAP,
                            color=INNER_COLOR)
                black_faces_behind_green_faces2.append(mybox)

        blue_faces = []
        black_faces_behind_blue_faces1 = []
        black_faces_behind_blue_faces2 = []
        for y in range(-1, 2):
            for z in range(-1, 2):
                mybox = box(pos=vector(-1.5 + GAP/2, y, z), length=THICKNESS, height=1 - GAP, width=1 - GAP, color=color.blue)
                blue_faces.append(mybox)
                mybox = box(pos=vector(-0.5 + GAP/2, y, z), length=THICKNESS, height=1 - GAP, width=1 - GAP, color=INNER_COLOR)
                black_faces_behind_blue_faces1.append(mybox)
                mybox = box(pos=vector(-0.5 - GAP/2, y, z), length=THICKNESS, height=1 - GAP, width=1 - GAP, color=INNER_COLOR)
                black_faces_behind_blue_faces2.append(mybox)

        red_faces = []
        black_faces_behind_red_faces1 = []
        black_faces_behind_red_faces2 = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                mybox = box(pos=vector(x, y, -1.5 + GAP/2), length=1 - GAP, height=1 - GAP, width=THICKNESS,
                            color=color.red)
                red_faces.append(mybox)
                mybox = box(pos=vector(x, y, -0.5 + GAP/2), length=1 - GAP, height=1 - GAP, width=THICKNESS,
                            color=INNER_COLOR)
                black_faces_behind_red_faces1.append(mybox)
                mybox = box(pos=vector(x, y, -0.5 - GAP/2), length=1 - GAP, height=1 - GAP, width=THICKNESS,
                            color=INNER_COLOR)
                black_faces_behind_red_faces2.append(mybox)

        yellow_faces = []
        black_faces_behind_yellow_faces1 = []
        black_faces_behind_yellow_faces2 = []
        for x in range(-1, 2):
            for z in range(-1, 2):
                mybox = box(pos=vector(x, -1.5 + GAP/2, z), length=1 - GAP, height=THICKNESS, width=1 - GAP,
                            color=color.yellow)
                yellow_faces.append(mybox)
                mybox = box(pos=vector(x, -0.5 + GAP/2, z), length=1 - GAP, height=THICKNESS, width=1 - GAP,
                            color=INNER_COLOR)
                black_faces_behind_yellow_faces1.append(mybox)
                mybox = box(pos=vector(x, -0.5 - GAP/2, z), length=1 - GAP, height=THICKNESS, width=1 - GAP,
                            color=INNER_COLOR)
                black_faces_behind_yellow_faces2.append(mybox)

        self.color_faces = orange_faces + white_faces + green_faces \
                           + blue_faces + red_faces + yellow_faces
        self.black_faces = black_faces_behind_orange_faces1 + black_faces_behind_orange_faces2 + \
                           black_faces_behind_white_faces1 + black_faces_behind_white_faces2 + \
                           black_faces_behind_green_faces1 + black_faces_behind_green_faces2 + \
                           black_faces_behind_blue_faces1 + black_faces_behind_blue_faces2 + \
                           black_faces_behind_red_faces1 + black_faces_behind_red_faces2 + \
                           black_faces_behind_yellow_faces1 + black_faces_behind_yellow_faces2
        self.all_faces = self.color_faces + self.black_faces

    def find_rotation_group(self, clicked_object, position, axis):
        mygroup = []
        for face in self.all_faces:
            if axis == 'y':
                if position is None:
                    position = clicked_object.pos.y
                if abs(face.pos.y - position) <= 0.5:
                    mygroup.append(face)
            elif axis == 'x':
                if position is None:
                    position = clicked_object.pos.x
                if abs(face.pos.x - position) <= 0.5:
                    mygroup.append(face)
            elif axis == 'z':
                if position is None:
                    position = clicked_object.pos.z
                if abs(face.pos.z - position) <= 0.5:
                    mygroup.append(face)
        return mygroup

    def rotate_90(self, group, axis):
        for i in range(30):
            rate(120)
            for b in group:
                b.rotate(angle=radians(3), axis=axis, origin=vector(0, 0, 0))

    def random_shuffle(self, n):
        if self.rotating:
            return

        self.rotating = True
        axes = ['x', 'y', 'z']
        for i in range(n):
            axis = axes[random.randint(0, 2)]
            pos = random.choice([-1, 1])
            if axis == 'x':
                group = self.find_rotation_group(None, pos, 'x')
                self.rotate_90(group, vector(1, 0, 0))
            elif axis == 'z':
                group = self.find_rotation_group(None, pos, 'z')
                self.rotate_90(group, vector(0, 0, 1))
            elif axis == 'y':
                group = self.find_rotation_group(None, pos, 'y')
                self.rotate_90(group, vector(0, 1, 0))

        self.rotating = False

    def face_colors(self, f):
        colors = []
        faces = []
        faces_final = []

        for face in self.color_faces:
            if f == 'front':
                if face.pos.z >= 1.5 - 2 * GAP:
                    faces.append(face)
            if f == 'right':
                if face.pos.x >= 1.5 - 2 * GAP:
                    faces.append(face)
            if f == 'left':
                if face.pos.x <= -1.5 + 2 * GAP:
                    faces.append(face)
            if f == 'back':
                if face.pos.z <= -1.5 + 2 * GAP:
                    faces.append(face)
            if f == 'up':
                if face.pos.y >= 1.5 - 2 * GAP:
                    faces.append(face)
            if f == 'down':
                if face.pos.y <= -1.5 + 2 * GAP:
                    faces.append(face)

        if f == 'up':
            faces = sorted(faces, key=lambda x: x.pos.z)
        elif f == 'down':
            faces = sorted(faces, key=lambda x: -x.pos.z)
        else:
            faces = sorted(faces, key=lambda x: -x.pos.y)

        def sort_key_func(face):
            if f == 'front':
                return face.pos.x
            if f == 'right':
                return -face.pos.z
            if f == 'left':
                return face.pos.z
            if f == 'back':
                return -face.pos.x
            if f == 'up':
                return face.pos.x
            if f == 'down':
                return face.pos.x

        faces_final.append(sorted(faces[:3], key=sort_key_func))
        faces_final.append(sorted(faces[3:6], key=sort_key_func))
        faces_final.append(sorted(faces[6:], key=sort_key_func))

        for row in faces_final:
            for face in row:
                if diff_angle(face.color, color.orange) < 0.01:
                    colors.append('orange')
                if diff_angle(face.color, color.white) <= 0.01:
                    colors.append('white')
                if diff_angle(face.color, color.red) <= 0.01:
                    colors.append('red')
                if diff_angle(face.color, color.blue) <= 0.01:
                    colors.append('blue')
                if diff_angle(face.color, color.green) <= 0.01:
                    colors.append('green')
                if diff_angle(face.color, vector(1,1,0)) <= 0.01:
                    colors.append('yellow')

        return [colors[:3], colors[3:6], colors[6:]]

    # Function that controls the self.movements
    def move(self, face):
        if face == "R":
            group = self.find_rotation_group(None, 1, 'x')
            self.rotate_90(group, vector(-1, 0, 0))

        if face == "R'":
            group = self.find_rotation_group(None, 1, 'x')
            self.rotate_90(group, vector(1, 0, 0))

        if face == "U":
            group = self.find_rotation_group(None, 1, 'y')
            self.rotate_90(group, vector(0, -1, 0))

        if face == "U'":
            group = self.find_rotation_group(None, 1, 'y')
            self.rotate_90(group, vector(0, 1, 0))

        if face == "D":
            group = self.find_rotation_group(None, -1, 'y')
            self.rotate_90(group, vector(0, 1, 0))

        if face == "D'":
            group = self.find_rotation_group(None, -1, 'y')
            self.rotate_90(group, vector(0, -1, 0))

        if face == "L":
            group = self.find_rotation_group(None, -1, 'x')
            self.rotate_90(group, vector(1, 0, 0))

        if face == "L'":
            group = self.find_rotation_group(None, -1, 'x')
            self.rotate_90(group, vector(-1, 0, 0))

        if face == "F":
            group = self.find_rotation_group(None, 1, 'z')
            self.rotate_90(group, vector(0, 0, -1))

        if face == "F'":
            group = self.find_rotation_group(None, 1, 'z')
            self.rotate_90(group, vector(0, 0, 1))

        if face == "B":
            group = self.find_rotation_group(None, -1, 'z')
            self.rotate_90(group, vector(0, 0, 1))

        if face == "B'":
            group = self.find_rotation_group(None, -1, 'z')
            self.rotate_90(group, vector(0, 0, -1))

        # whole cube clockwise rotation
        if face == "ALL":
            self.rotate_90(self.all_faces, vector(0, -1, 0))

    def get_corner_face_colors(self, corner_code):
        if corner_code == 'ufr':
            return [self.face_colors('up'[2][2], self.face_colors('front', [0][2]), self.face_colors('right', [0][0]))]
        if corner_code == 'ufl':
            return [self.face_colors('up'[2][2], self.face_colors('front', [0][2]), self.face_colors('left', [0][0]))]
        if corner_code == 'ubr':
            return [self.face_colors('up'[2][2], self.face_colors('back', [0][2]), self.face_colors('right', [0][0]))]
        if corner_code == 'ubl':
            return [self.face_colors('up'[2][2], self.face_colors('back', [0][2]), self.face_colors('left', [0][0]))]

    def little_face_color_at(self, face_code):
        # 'dr_d' means the little face at the down of the down right cube
        if face_code == 'dr_d':
            return self.face_colors('down')[1][2]
        if face_code == 'dr_r':
            return self.face_colors('right')[2][1]

        if face_code == 'db_d':
            return self.face_colors('down')[2][1]
        if face_code == 'db_b':
            return self.face_colors('back')[2][1]

        if face_code == 'dl_d':
            return self.face_colors('down')[1][0]
        if face_code == 'dl_l':
            return self.face_colors('left')[2][1]

        if face_code == 'df_d':
            return self.face_colors('down')[0][1]
        if face_code == 'df_f':
            return self.face_colors('front')[2][1]

        if face_code == 'fr_f':
            return self.face_colors('front')[1][2]
        if face_code == 'fr_r':
            return self.face_colors('right')[1][0]

        if face_code == 'fl_f':
            return self.face_colors('front')[1][0]
        if face_code == 'fl_l':
            return self.face_colors('left')[1][2]

        if face_code == 'br_b':
            return self.face_colors('back')[1][0]
        if face_code == 'br_r':
            return self.face_colors('right')[1][2]

        if face_code == 'bl_b':
            return self.face_colors('back')[1][2]
        if face_code == 'bl_l':
            return self.face_colors('left')[1][0]

        if face_code == 'uf_u':
            return self.face_colors('up')[2][1]
        if face_code == 'uf_f':
            return self.face_colors('front')[0][1]

        if face_code == 'ur_u':
            return self.face_colors('up')[1][2]
        if face_code == 'ur_r':
            return self.face_colors('right')[0][1]

        if face_code == 'ul_u':
            return self.face_colors('up')[1][0]
        if face_code == 'ul_l':
            return self.face_colors('left')[0][1]

        if face_code == 'ub_u':
            return self.face_colors('up')[0][1]
        if face_code == 'ub_b':
            return self.face_colors('back')[0][1]

        if face_code == 'ufl_u':
            return self.face_colors('up')[2][0]
        if face_code == 'ufl_f':
            return self.face_colors('front')[0][0]
        if face_code == 'ufl_l':
            return self.face_colors('left')[0][2]

        if face_code == 'ufr_u':
            return self.face_colors('up')[2][2]
        if face_code == 'ufr_f':
            return self.face_colors('front')[0][2]
        if face_code == 'ufr_r':
            return self.face_colors('right')[0][0]

        if face_code == 'ubl_u':
            return self.face_colors('up')[0][0]
        if face_code == 'ubl_b':
            return self.face_colors('back')[0][2]
        if face_code == 'ubl_l':
            return self.face_colors('left')[0][0]

        if face_code == 'ubr_u':
            return self.face_colors('up')[0][2]
        if face_code == 'ubr_b':
            return self.face_colors('back')[0][0]
        if face_code == 'ubr_r':
            return self.face_colors('right')[0][2]

        if face_code == 'dfl_d':
            return self.face_colors('down')[0][0]
        if face_code == 'dfl_f':
            return self.face_colors('front')[0][2]
        if face_code == 'dfl_l':
            return self.face_colors('left')[2][2]

        if face_code == 'dfr_d':
            return self.face_colors('down')[0][2]
        if face_code == 'dfr_f':
            return self.face_colors('front')[2][2]
        if face_code == 'dfr_r':
            return self.face_colors('right')[2][0]

        if face_code == 'dbl_d':
            return self.face_colors('down')[2][0]
        if face_code == 'dbl_b':
            return self.face_colors('back')[2][2]
        if face_code == 'dbl_l':
            return self.face_colors('left')[2][0]

        if face_code == 'dbr_d':
            return self.face_colors('down')[2][2]
        if face_code == 'dbr_b':
            return self.face_colors('back')[2][0]
        if face_code == 'dbr_r':
            return self.face_colors('right')[2][2]

    def solving_white_cross(self):
        colors = ['orange', 'green', 'red', 'blue']

        print('solving white cross')
        for color in colors:
            if self.little_face_color_at('dr_d') == 'white' and self.little_face_color_at('dr_r') == color:
                self.move("R")
                self.move("R")
                self.move("U")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('db_d') == 'white' and self.little_face_color_at('db_b') == color:
                self.move("B")
                self.move("B")
                self.move("U")
                self.move("U")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('dl_d') == 'white' and self.little_face_color_at('dl_l') == color:
                self.move("L")
                self.move("L")
                self.move("U'")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('fr_f') == 'white' and self.little_face_color_at('fr_r') == color:
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('fl_f') == 'white' and self.little_face_color_at('fl_l') == color:
                self.move("L'")
                self.move("U'")
                self.move("L")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('br_b') == 'white' and self.little_face_color_at('br_r') == color:
                self.move("R'")
                self.move("U")
                self.move("R")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('bl_b') == 'white' and self.little_face_color_at('bl_l') == color:
                self.move("L")
                self.move("U'")
                self.move("L'")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('uf_u') == 'white' and self.little_face_color_at('uf_f') == color:
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('ur_u' == 'white') and self.little_face_color_at('ur_r') == color:
                self.move("U")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('ul_u') == 'white' and self.little_face_color_at('ul_l') == color:
                self.move("U'")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('ub_u') == 'white' and self.little_face_color_at('ub_b') == color:
                self.move("U")
                self.move("U")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('dr_d') == color and self.little_face_color_at('dr_r') == 'white':
                self.move("R")
                self.move("F")

            elif self.little_face_color_at('db_d') == color and self.little_face_color_at('db_b') == 'white':
                self.move("B")
                self.move("D")
                self.move("R")
                self.move("D'")

            elif self.little_face_color_at('dl_d') == color and self.little_face_color_at('dl_l') == 'white':
                self.move("L'")
                self.move("F'")

            elif self.little_face_color_at('fr_f') == color and self.little_face_color_at('fr_r') == 'white':
                self.move("F")

            elif self.little_face_color_at('fl_f') == color and self.little_face_color_at('fl_l') == 'white':
                self.move("F'")

            elif self.little_face_color_at('br_b') == color and self.little_face_color_at('br_r') == 'white':
                self.move("B")
                self.move("U")
                self.move("U")
                self.move("B'")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('bl_b') == color and self.little_face_color_at('bl_l') == 'white':
                self.move("B'")
                self.move("U")
                self.move("U")
                self.move("B")
                self.move("F")
                self.move("F")

            elif self.little_face_color_at('uf_u') == color and self.little_face_color_at('uf_f') == 'white':
                self.move("U'")
                self.move("R'")
                self.move("F")
                self.move("R")

            elif self.little_face_color_at('ur_u') == color and self.little_face_color_at('ur_r') == 'white':
                self.move("R'")
                self.move("F")
                self.move("R")

            elif self.little_face_color_at('ul_u') == color and self.little_face_color_at('ul_l') == 'white':
                self.move("L")
                self.move("F'")
                self.move("L'")

            elif self.little_face_color_at('ub_u') == color and self.little_face_color_at('ub_b') == 'white':
                self.move("U")
                self.move("R'")
                self.move("F")
                self.move("R")

            elif self.little_face_color_at('df_d') == color and self.little_face_color_at('df_f') == 'white':
                self.move("F'")
                self.move("D")
                self.move("R'")
                self.move("D'")

            self.move('ALL')

        for color in colors:
            self.move("F")
            self.move("F")
            self.move('ALL')

    def solving_white_corners(self):
        self.rotate_90(self.all_faces, vector(1, 0, 0))
        self.rotate_90(self.all_faces, vector(1, 0, 0))

        print("Solving the white corners")
        colors = [['white', 'red', 'green'], ['white', 'green', 'orange'],
                  ['white', 'orange', 'blue'], ['white', 'blue', 'red']]

        for color_list in colors:
            if self.little_face_color_at('ufl_u') in color_list \
                    and self.little_face_color_at('ufl_f') in color_list \
                    and self.little_face_color_at('ufl_l') in color_list:
                self.move("U'")

            elif self.little_face_color_at('ubl_u') in color_list \
                    and self.little_face_color_at('ubl_b') in color_list \
                    and self.little_face_color_at('ubl_l') in color_list:
                self.move("U'")
                self.move("U'")

            elif self.little_face_color_at('ubr_u') in color_list \
                    and self.little_face_color_at('ubr_b') in color_list \
                    and self.little_face_color_at('ubr_r') in color_list:
                self.move("U")

            elif self.little_face_color_at('dfl_d') in color_list \
                    and self.little_face_color_at('dfl_f') in color_list \
                    and self.little_face_color_at('dfl_l') in color_list:
                self.move("L'")
                self.move("U'")
                self.move("L")

            elif self.little_face_color_at('dbl_d') in color_list \
                    and self.little_face_color_at('dbl_b') in color_list \
                    and self.little_face_color_at('dbl_l') in color_list:
                self.move("L")
                self.move("U")
                self.move("U")
                self.move("L'")

            elif self.little_face_color_at('dbr_d') in color_list \
                   and self.little_face_color_at('dbr_b') in color_list \
                   and self.little_face_color_at('dbr_r') in color_list:
                self.move("R'")
                self.move("U")
                self.move("R")
                self.move("U")

            if self.little_face_color_at('dfr_r') == 'white' \
                    and self.little_face_color_at('dfr_d') in color_list \
                    and self.little_face_color_at('dfr_f') in color_list:
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("R")
                self.move("U")
                self.move("R'")

            if self.little_face_color_at('dfr_f') == 'white' \
                    and self.little_face_color_at('dfr_d') in color_list \
                    and self.little_face_color_at('dfr_r') in color_list:
                self.move("F'")
                self.move("U'")
                self.move("F")
                self.move("U")
                self.move("F'")
                self.move("U'")
                self.move("F")

            if self.little_face_color_at('ufr_u') == 'white' \
                    and self.little_face_color_at('ufr_f') in color_list \
                    and self.little_face_color_at('ufr_r') in color_list:
                self.move("R")
                self.move("U")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("R")
                self.move("U")
                self.move("R'")

            if self.little_face_color_at('ufr_f') == 'white' \
                    and self.little_face_color_at('ufr_u') in color_list \
                    and self.little_face_color_at('ufr_r') in color_list:
                self.move("U")
                self.move("R")
                self.move("U'")
                self.move("R'")

            if self.little_face_color_at('ufr_r') == 'white' \
                    and self.little_face_color_at('ufr_u') in color_list \
                    and self.little_face_color_at('ufr_f') in color_list:
                self.move("R")
                self.move("U")
                self.move("R'")

            self.move('ALL')

        self.rotate_90(self.all_faces, vector(-1, 0, 0))
        self.rotate_90(self.all_faces, vector(-1, 0, 0))


    def solving_second_stage(self):
        self.rotate_90(self.all_faces, vector(1, 0, 0))
        self.rotate_90(self.all_faces, vector(1, 0, 0))

        print("Solving the second stage")
        colors = [['red', 'green'], ['green', 'orange'],
                  ['orange', 'blue'], ['blue', 'red']]

        for colors_list in colors:
            if self.little_face_color_at('fl_f') in colors_list and self.little_face_color_at('fl_l') in colors_list:
                self.move("F")
                self.move("U")
                self.move("F'")
                self.move("U'")
                self.move("L'")
                self.move("U'")
                self.move("L")

            if self.little_face_color_at('br_b') in colors_list and self.little_face_color_at('br_r') in colors_list:
                self.move('ALL')
                self.move('ALL')
                self.move("F")
                self.move("U")
                self.move("F'")
                self.move("U'")
                self.move("L'")
                self.move("U'")
                self.move("L")
                self.move('ALL')
                self.move('ALL')

            if self.little_face_color_at('bl_b') in colors_list and self.little_face_color_at('bl_l') in colors_list:
                self.move('ALL')
                self.move('ALL')
                self.move('ALL')
                self.move("F")
                self.move("U")
                self.move("F'")
                self.move("U'")
                self.move("L'")
                self.move("U'")
                self.move("L")
                self.move('ALL')

            if self.little_face_color_at('fr_r') is colors_list[0] and self.little_face_color_at('fr_f') in colors_list:
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("U'")
                self.move("R")
                self.move("U'")
                self.move("U'")
                self.move("R'")
                self.move("U")
                self.move("F'")
                self.move("U'")
                self.move("F")

            if self.little_face_color_at('uf_f') is colors_list[0] and self.little_face_color_at('uf_u') in colors_list:
                self.move("U")
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("F'")
                self.move("U'")
                self.move("F")

            if self.little_face_color_at('uf_u') is colors_list[0] and self.little_face_color_at('uf_f') in colors_list:
                self.move("U'")
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U")
                self.move("R")
                self.move("U")
                self.move("R")

            if self.little_face_color_at('ur_u') is colors_list[0] and self.little_face_color_at('ur_r') in colors_list:
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U")
                self.move("R")
                self.move("U")
                self.move("R")

            if self.little_face_color_at('ur_r') is colors_list[0] and self.little_face_color_at('ur_u') in colors_list:
                self.move("U")
                self.move("U")
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("F'")
                self.move("U'")
                self.move("F")

            if self.little_face_color_at('ub_b') is colors_list[0] and self.little_face_color_at('ub_u') in colors_list:
                self.move("U'")
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("F'")
                self.move("U'")
                self.move("F")

            if self.little_face_color_at('ub_u') is colors_list[0] and self.little_face_color_at('ub_b') in colors_list:
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U")
                self.move("R")
                self.move("U")
                self.move("R")

            if self.little_face_color_at('ul_l') is colors_list[0] and self.little_face_color_at('ul_u') in colors_list:
                self.move("R")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("F'")
                self.move("U'")
                self.move("F")

            if self.little_face_color_at('ul_u') is colors_list[0] and self.little_face_color_at('ul_l') in colors_list:
                self.move("U")
                self.move("U")
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U'")
                self.move("R'")
                self.move("U")
                self.move("R")
                self.move("U")
                self.move("R")

            if self.little_face_color_at('fr_f') is colors_list[0] and self.little_face_color_at('fr_r') in colors_list:
                print("The edge and its corners has been built.")

            self.move('ALL')

        self.rotate_90(self.all_faces, vector(-1, 0, 0))
        self.rotate_90(self.all_faces, vector(-1, 0, 0))

    def solving_yellow_cross(self):
        self.rotate_90(self.all_faces, vector(1, 0, 0))
        self.rotate_90(self.all_faces, vector(1, 0, 0))

        if self.little_face_color_at('uf_u') != 'yellow' and self.little_face_color_at('ur_u') != 'yellow' and \
                self.little_face_color_at('ub_u') != 'yellow' and self.little_face_color_at('ul_u') != 'yellow':  # If the point is yellow then :
            self.move("R'")
            self.move("U'")
            self.move("F'")
            self.move("U")
            self.move("F")
            self.move("R")

        if self.little_face_color_at('uf_u') != 'yellow' and self.little_face_color_at('ub_u') != 'yellow' and \
                self.little_face_color_at('ur_u') == 'yellow' and self.little_face_color_at('ul_u') == 'yellow':  # If the yellow line is finished :
            self.move("R'")
            self.move("U'")
            self.move("F'")
            self.move("U")
            self.move("F")
            self.move("R")

        if self.little_face_color_at('ur_u') != 'yellow' and self.little_face_color_at('ul_u') != 'yellow' and \
                self.little_face_color_at('uf_u') == 'yellow' and self.little_face_color_at('ub_u') == 'yellow':  # Otherwise :
            self.move("U")  # Simple rotation of the top face to adjust the yellow line
            self.move("R'")
            self.move("U'")
            self.move("F'")
            self.move("U")
            self.move("F")
            self.move("R")

        if self.little_face_color_at('uf_u') != 'yellow' and self.little_face_color_at('ur_u') != 'yellow' and \
                self.little_face_color_at('ub_u') == 'yellow' and self.little_face_color_at('ul_u') == 'yellow':  # If the yellow "L" shape is finished :
            self.move("R'")
            self.move("U'")
            self.move("F'")
            self.move("U")
            self.move("F")
            self.move("R")

        if self.little_face_color_at('uf_u') != 'yellow' and self.little_face_color_at('ur_u') == 'yellow' and \
                self.little_face_color_at('ub_u') == 'yellow' and self.little_face_color_at('ul_u') != 'yellow':  # Otherwise :
            self.move("U'")
            self.move("R'")
            self.move("U'")
            self.move("F'")
            self.move("U")
            self.move("F")
            self.move("R")

        if self.little_face_color_at('uf_u') == 'yellow' and self.little_face_color_at('ur_u') == 'yellow' and \
                self.little_face_color_at('ub_u') != 'yellow' and self.little_face_color_at('ul_u') != 'yellow':
            self.move("U")
            self.move("U")
            self.move("R'")
            self.move("U'")
            self.move("F'")
            self.move("U")
            self.move("F")
            self.move("R")

        if self.little_face_color_at('uf_u') == 'yellow' and self.little_face_color_at('ur_u') != 'yellow' and \
                self.little_face_color_at('ub_u') != 'yellow' and self.little_face_color_at('ul_u') == 'yellow':
            self.move("U")
            self.move("R'")
            self.move("U'")
            self.move("F'")
            self.move("U")
            self.move("F")
            self.move("R")

        # The cross is built !

        # Adjusting the colors
        loop = 1  # Are the colors in their position ? The loop variable is used to answer the question
        while loop:
            if self.little_face_color_at('uf_f') == 'red' and self.little_face_color_at('ur_r') == 'green':
                self.move("U")
                self.move("U")

            elif self.little_face_color_at('ul_l') == 'red' and self.little_face_color_at('uf_f') == 'green':
                self.move("U")

            elif self.little_face_color_at('ur_r') == 'red' and self.little_face_color_at('ub_b') == 'green':
                self.move("U'")

            if self.little_face_color_at('uf_f') == 'green' and self.little_face_color_at('ur_r') == 'orange':
                self.move("U")
                self.move("U")

            elif self.little_face_color_at('ul_l') == 'green' and self.little_face_color_at('uf_f') == 'orange':
                self.move("U")

            elif self.little_face_color_at('ur_r') == 'green' and self.little_face_color_at('ub_b') == 'orange':
                self.move("U'")

            if self.little_face_color_at('uf_f') == 'orange' and self.little_face_color_at('ur_r') == 'blue':
                self.move("U")
                self.move("U")

            elif self.little_face_color_at('ul_l') == 'orange' and self.little_face_color_at('uf_f') == 'blue':
                self.move("U")

            elif self.little_face_color_at('ur_r') == 'orange' and self.little_face_color_at('ub_b') == 'blue':
                self.move("U'")

            if self.little_face_color_at('uf_f') == 'blue' and self.little_face_color_at('ur_r') == 'red':
                self.move("U")
                self.move("U")

            elif self.little_face_color_at('ul_l') == 'blue' and self.little_face_color_at('uf_f') == 'red':
                self.move("U")

            elif self.little_face_color_at('ur_r') == 'blue' and self.little_face_color_at('ub_b') == 'red':
                self.move("U'")

            # Technical algorithm
            self.move("U")
            self.move("R")
            self.move("U")
            self.move("R'")
            self.move("U")
            self.move("R")
            self.move("U")
            self.move("U")
            self.move("R'")

            # Testing the Rubik's cube to know if the colors can be placed only by "U" self.moves
            if self.little_face_color_at('ul_l') == 'red' and self.little_face_color_at('uf_f') == 'green' and \
                    self.little_face_color_at('ur_r') == 'orange' and self.little_face_color_at('ub_b') == 'blue':
                self.move("U'")
            if self.little_face_color_at('ul_l') == 'orange' and self.little_face_color_at('uf_f') == 'blue' and \
                    self.little_face_color_at('ur_r') == 'red' and self.little_face_color_at('ub_b') == 'green':
                self.move("U")
            if self.little_face_color_at('ul_l') == 'green' and self.little_face_color_at('uf_f') == 'orange' and \
                    self.little_face_color_at('ur_r') == 'blue' and self.little_face_color_at('ub_b') == 'red':
                self.move("U")
                self.move("U")
            if self.little_face_color_at('ul_l') == 'blue' and self.little_face_color_at('uf_f') == 'red' and \
                    self.little_face_color_at('ur_r') == 'green' and self.little_face_color_at('ub_b') == 'orange':
                loop = 0  # If the cross/colors are correctly placed, we exit the loop

        self.rotate_90(self.all_faces, vector(-1, 0, 0))
        self.rotate_90(self.all_faces, vector(-1, 0, 0))

        def solving_final(self):
            print("Solving the yellow corners")

            while True:
                if ('r' in self.get_corner_face_colors('ufr') and 'g' in self.get_corner_face_colors('ufr')) and \
                    ('b' in self.get_corner_face_colors('ufl') and 'r' in self.get_corner_face_colors('ufl')) and \
                    ('g' in self.get_corner_face_colors('ubr') and 'o' in self.get_corner_face_colors('ubr')) and \
                    ('b' in self.get_corner_face_colors('ubl') and 'o' in self.get_corner_face_colors('ubl')):
                    break

                if 'g' in ubr.values() and 'o' in ubr.values():  # If green/orange are contained in the values of ubr (up-back-right) then :
                    self.move("U")
                    self.move("U")
                    self.move("R")
                    self.move("U'")
                    self.move("L'")
                    self.move("U")
                    self.move("R'")
                    self.move("U'")
                    self.move("L")
                    self.move("U'")

                elif 'r' in ufr.values() and 'g' in ufr.values():
                    self.move("U")
                    self.move("R")
                    self.move("U'")
                    self.move("L'")
                    self.move("U")
                    self.move("R'")
                    self.move("U'")
                    self.move("L")

                elif 'b' in ubl.values() and 'o' in ubl.values():
                    self.move("U'")
                    self.move("R")
                    self.move("U'")
                    self.move("L'")
                    self.move("U")
                    self.move("R'")
                    self.move("U'")
                    self.move("L")
                    self.move("U")
                    self.move("U")

                elif 'b' in ufl.values() and 'r' in ufl.values():
                    self.move("R")
                    self.move("U'")
                    self.move("L'")
                    self.move("U")
                    self.move("R'")
                    self.move("U'")
                    self.move("L")
                    self.move("U")

                else:
                    self.move("U")
                    self.move("R")
                    self.move("U'")
                    self.move("L'")
                    self.move("U")
                    self.move("R'")
                    self.move("U'")
                    self.move("L")

            while 1:
                if ufr['u'] == 'y':  # If the yellow color of the Rubik's cube is on top
                    if ended():  # If the RC is resolved
                        break

                    self.move("U'")  # Moving to the next hut

                if ufr['r'] == 'y':  # If the yellow color of the hut is on the right of the RC
                    self.move("R'")
                    self.move("D'")
                    self.move("R")
                    self.move("D")

                    self.move("R'")
                    self.move("D'")
                    self.move("R")
                    self.move("D")

                if ufr['f'] == 'y':  # If it's in the front (face):
                    self.move("R'")
                    self.move("D'")
                    self.move("R")
                    self.move("D")

                    self.move("R'")
                    self.move("D'")
                    self.move("R")
                    self.move("D")

                    self.move("R'")
                    self.move("D'")
                    self.move("R")
                    self.move("D")

                    self.move("R'")
                    self.move("D'")
                    self.move("R")
                    self.move("D")


def mouse_down_callback():
    if cube.rotating:
        return
    cube.rotating = True
    clicked_object = scene.mouse.pick
    if clicked_object is not None and not clicked_object.color.equals(INNER_COLOR):
        if scene.mouse.shift:
            group = cube.find_rotation_group(clicked_object, None, 'x')
            cube.rotate_90(group, vector(1, 0, 0))
        elif scene.mouse.alt:
            group = cube.find_rotation_group(clicked_object, None, 'z')
            cube.rotate_90(group, vector(0, 0, 1))
        else:
            group = cube.find_rotation_group(clicked_object, None, 'y')
            cube.rotate_90(group, vector(0, 1, 0))
    cube.rotating = False


def key_down_callback(evt):
    s = evt.key
    if s == 's':
        cube.random_shuffle(30)
    if s == 'f':
        print(cube.face_colors('front'))
    if s == 'r':
        print(cube.face_colors('right'))
    if s == 'l':
        print(cube.face_colors('left'))
    if s == 'b':
        print(cube.face_colors('back'))
    if s == 't':
        print(cube.face_colors('up'))
    if s == 'd':
        print(cube.face_colors('down'))
    if s == 'a':
        cube.solving_white_cross()
        cube.solving_white_corners()
        cube.solving_second_stage()
        cube.solving_yellow_cross()


cube = RubiksCube()
scene.background = color.gray(0.2)
scene.center = vector(0,0,0)
scene.userzoom = False
scene.userpan = False
scene.forward = vector(-0.9,-1,-1)
scene.range = 4
scene.autoscale = False
scene.bind('mousedown', mouse_down_callback)
scene.bind('keydown', key_down_callback)
cube.random_shuffle(20)
