class BadStartName(Exception):
    pass


class BoardPiece:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def setPosition(self, x, y):
        # position is top left corner
        self.x = x
        self.y = y

    def printme(self):
        print(f'I am {self.name}')
        print(f'My position is ({self.x}, {self.y})')


class HuaRongDao:
    def initialize_hengdaolima(self):
        self.pieces = []
        caocao = BoardPiece('Cao Cao', 2, 2)
        caocao.setPosition(1, 0)
        self.pieces.append(caocao)

        huangzhong = BoardPiece('Huang Zhong', 1, 2)
        huangzhong.setPosition(0, 0)
        self.pieces.append(huangzhong)

        zhoayun = BoardPiece('Zhoa Yun', 1, 2)
        zhoayun.setPosition(3, 0)
        self.pieces.append(zhoayun)

        zhangfei = BoardPiece('Zhang Fei', 1, 2)
        zhangfei.setPosition(0, 2)
        self.pieces.append(zhangfei)

        macao = BoardPiece('Ma Cao', 1, 2)
        macao.setPosition(3, 2)
        self.pieces.append(macao)

        guanyu = BoardPiece('Guan Yu', 2, 1)
        guanyu.setPosition(1, 2)
        self.pieces.append(guanyu)

        for i in range(4):
            zu = BoardPiece('Zu', 1, 1)
            if i == 0 or i == 3:
                zu.setPosition(i, 4)
            else:
                zu.setPosition(i, 3)
            self.pieces.append(zu)

        for i in range(2):
            empty_space = BoardPiece('Blank', 1, 1)
            empty_space.setPosition(i+1, 4)
            self.pieces.append(empty_space)

    def __init__(self, start_name):
        if start_name == 'hengdaolima':
            self.initialize_hengdaolima()
        else:
            raise BadStartName()

    def check_move(self, piece, empty_space, empty_space_state):
        moves = []
        if piece.height + piece.y == empty_space.y and piece.x == empty_space.x:
            if piece.width == 1:
                moves.append((piece, (0, 1)))
                if empty_space_state == 'v':
                    moves.append((piece, (0, 2)))
            else:
                if empty_space_state == 'h':
                    moves.append((piece, (0, 1)))
        elif empty_space.y + 1 == piece.y and piece.x == empty_space.x:
            if piece.width == 1:
                moves.append((piece, (0, -1)))
                if empty_space_state == 'v':
                    moves.append((piece, (0, -2)))
            else:
                if empty_space_state == 'h':
                    moves.append((piece, (0, -1)))

        if piece.width + piece.x == empty_space.x and piece.y == empty_space.y:
            if piece.height == 1:
                moves.append((piece, (1, 0)))
                if empty_space_state == 'h':
                    moves.append((piece, (2, 0)))
            else:
                if empty_space_state == 'v':
                    moves.append((piece, (1, 0)))
        elif empty_space.x + 1 == piece.x and piece.y == empty_space.y:
            if piece.height == 1:
                moves.append((piece, (-1, 0)))
                if empty_space_state == 'h':
                    moves.append((piece, (-2, 0)))
            else:
                if empty_space_state == 'h':
                    moves.append((piece, (-1, 0)))
        return moves

    def find_possible_moves(self):
        """
        return: a list of possible moves. Each move is a tuple.
        First element of the tuple is the piece to move,
        second element of the tuple is a vector represented by a tuple
        """
        possible_moves = []
        empty_spaces = []
        for p in self.pieces:
            if p.name == 'Blank':
                empty_spaces.append(p)

        # three possible values 'h', 'v', 's'
        # horizontal
        # vertical
        # separate
        empty_space_state = None

        if empty_spaces[0].y == empty_spaces[1].y and abs(empty_spaces[0].x-empty_spaces[1].x) == 1:
            empty_space_state = 'h'
        elif empty_spaces[0].x == empty_spaces[1].x and abs(empty_spaces[0].y-empty_spaces[1].y) == 1:
            empty_space_state = 'v'
        else:
            empty_space_state = 's'

        print(empty_space_state)

        all_moves = []
        for piece in self.pieces:
            if piece.name != 'Blank':
                all_moves += self.check_move(piece, empty_spaces[0], empty_space_state)
                all_moves += self.check_move(piece, empty_spaces[1], empty_space_state)

        all_moves = list(set(all_moves))

        for move in all_moves:
            print(move[0].name, move[0].x, move[0].y)
            print(move[1])

        return all_moves

if __name__ == "__main__":
    huarongdao = HuaRongDao('hengdaolima')
    huarongdao.find_possible_moves()
