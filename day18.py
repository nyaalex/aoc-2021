from advent import AdventDay


class SnailPair:
    LEFT = 0
    RIGHT = 1

    def __repr__(self):
        return '[%s,%s]' % (repr(self.left), repr(self.right))

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.base = False

    def can_split(self):
        return False

    def can_explode(self):
        return self.left.base and self.right.base

    def explode(self):
        return self.left.value, self.right.value

    def get_magnitude(self):
        l_mag = self.left.get_magnitude()
        r_mag = self.right.get_magnitude()
        return 3 * l_mag + 2 * r_mag

    def base_add(self, value, side, jumped=False):
        if side == self.LEFT:
            self.left.base_add(value, side)
        elif side == self.RIGHT:
            self.right.base_add(value, side)

    def reduce_step(self, depth=0):
        changed, data = self.left.reduce_step(depth+1)
        if changed:
            if data:
                val, side = data
                if side == self.RIGHT:
                    self.right.base_add(val, self.LEFT)
                    return True, None
            return True, data

        # check if reduction is necessary
        if self.left.can_explode() and depth >= 3:
            left, right = self.left.explode()
            self.left = SnailBase(0)
            self.right.base_add(right, self.LEFT)
            return True, (left, self.LEFT)

        if self.left.can_split():
            self.left = self.left.split()
            return True, None

        changed, data = self.right.reduce_step(depth + 1)
        if changed:
            if data:
                val, side = data
                if side == self.LEFT:
                    self.left.base_add(val, self.RIGHT)
                    return True, None
            return True, data

        if self.right.can_explode() and depth >= 3:
            left, right = self.right.explode()
            self.right = SnailBase(0)
            self.left.base_add(left, self.RIGHT)
            return True, (right, self.RIGHT)

        if self.right.can_split():
            self.right = self.right.split()
            return True, None

        return False, None

    def add(self, other):
        l, r = self.left, self.right
        self.left = SnailPair(l, r)
        self.right = other

        steps = []
        changed = True
        while changed:
            steps.append(repr(self))
            changed, _ = self.reduce_step()

        return steps


class SnailBase(SnailPair):

    def __repr__(self):
        return repr(self.value)

    def __init__(self, value):
        super().__init__(None, None)
        self.value = value
        self.base = True

    def get_magnitude(self):
        return self.base

    def can_split(self):
        return self.value > 9

    def can_explode(self):
        return False

    def base_add(self, value, side, jumped=False):
        self.value += value

    def split(self):
        left = self.value//2
        right = self.value - left
        left, right = SnailBase(left), SnailBase(right)
        return SnailPair(left, right)

    def reduce_step(self, depth=0):
        return False, None


def parse_pair(pairs):
    pairs = pairs[1:-1]
    left_string, right_string = '', ''
    depth = 0
    is_left = True
    for c in pairs:
        if depth == 0 and c == ',':
            is_left = False
            continue

        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1

        if is_left:
            left_string += c
        else:
            right_string += c

    if left_string[0] == '[':
        left = parse_pair(left_string)
    else:
        left = SnailBase(int(left_string))

    if right_string[0] == '[':
        right = parse_pair(right_string)
    else:
        right = SnailBase(int(right_string))

    return SnailPair(left, right)


class Day18(AdventDay):

    def __init__(self):
        super().__init__(2021, 18)

    def part_1(self):
        inp = self.read_lines()
        first = parse_pair(inp.pop(0))

        for line in inp:
            first.add(parse_pair(line))
            print(first)

        print(first)
        return first.get_magnitude()

    def part_2(self):
        pass


if __name__ == '__main__':
    d18 = Day18()
    d18.day_input = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'''
# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# [7,[5,[[3,8],[1,4]]]]
# [[2,[2,2]],[8,[8,1]]]
# [2,9]
# [1,[[[9,3],9],[[9,0],[0,7]]]]
# [[[5,[7,4]],7],1]
# [[[[4,2],2],6],[8,7]]'''
    d18.main()
