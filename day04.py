from advent import AdventDay


class BingoBoard:

    def __init__(self, board):
        self._val_lookup = {}
        self._unmarked = set()

        self._build_board(board)
        self._lines = [0 for _ in range(10)]

    def _build_board(self, input_board):
        for x in range(5):
            for y in range(5):
                val = input_board[x][y]
                self._val_lookup[val] = (x, y)
                self._unmarked.add(val)

    def mark(self, num):
        if num not in self._val_lookup:
            return 0

        self._unmarked.remove(num)
        x, y = self._val_lookup[num]
        self._lines[x] += 1
        self._lines[y + 5] += 1

        if 5 in (self._lines[y + 5], self._lines[x]):
            return sum(self._unmarked) * num
        else:
            return 0


class Day4(AdventDay):

    def __init__(self):
        super().__init__(2021, 4)

    def get_boards(self):
        inp = self.parse_ints()

        boards = []
        to_call = inp.pop(0)

        board = []
        for line in inp:
            if len(line) == 0:
                continue

            if len(board) == 5:
                boards.append(BingoBoard(board))
                board = []

            board.append(line)

        return to_call, boards

    def part_1(self):
        to_call, boards = self.get_boards()

        for called in to_call:
            for board in boards:
                result = board.mark(called)
                if result:
                    return result
        
    def part_2(self):
        to_call, boards = self.get_boards()

        for called in to_call:
            new_boards = boards.copy()

            for board in boards:
                result = board.mark(called)

                if result and len(boards) == 1:
                    return result
                elif result:
                    new_boards.remove(board)

            boards = new_boards




if __name__ == '__main__':
    d4 = Day4()
    d4.main()
