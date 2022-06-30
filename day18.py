from advent import AdventDay


class SnailPair:
    LEFT = 0
    RIGHT = 1

    def __repr__(self):
        return '[%s,%s]' % (repr(self.left), repr(self.right))

    def debug_string(self, depth=0):
        return '[%s%s,%s]' % ('!' if depth > 3 else '',
                              self.left.debug_string(depth + 1),
                              self.right.debug_string(depth + 1))

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

    def explode_step(self, depth=0):
        changed, data = self.left.explode_step(depth + 1)
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

        if self.right.can_explode() and depth >= 3:
            left, right = self.right.explode()
            self.right = SnailBase(0)
            self.left.base_add(left, self.RIGHT)
            return True, (right, self.RIGHT)

        changed, data = self.right.explode_step(depth + 1)
        if changed:
            if data:
                val, side = data
                if side == self.LEFT:
                    self.left.base_add(val, self.RIGHT)
                    return True, None
            return True, data

        return False, None

    def split_step(self, depth=0):
        changed = self.left.split_step(depth + 1)
        if changed:
            return True

        if self.left.can_split():
            self.left = self.left.split()
            return True

        if self.right.can_split():
            self.right = self.right.split()
            return True

        changed = self.right.split_step(depth + 1)
        if changed:
            return True

    def add(self, other):
        l, r = self.left, self.right
        self.left = SnailPair(l, r)
        self.right = other

        changed = True
        while changed:

            changed, _ = self.explode_step()
            if changed:
                continue
            else:
                changed = self.split_step()


class SnailBase(SnailPair):

    def __repr__(self):
        return repr(self.value)

    def debug_string(self, depth=0):
        return repr(self.value)

    def __init__(self, value):
        super().__init__(None, None)
        self.value = value
        self.base = True

    def get_magnitude(self):
        return self.value

    def can_split(self):
        return self.value > 9

    def can_explode(self):
        return False

    def base_add(self, value, side, jumped=False):
        self.value += value

    def split(self):
        left = self.value // 2
        right = self.value - left
        left, right = SnailBase(left), SnailBase(right)
        return SnailPair(left, right)

    def explode_step(self, depth=0):
        return False, None

    def split_step(self, depth=0):
        return False


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

        return first.get_magnitude()

    def part_2(self):
        inp = self.read_lines()

        max_add = 0
        for x in inp:
            for y in inp:
                tmp = parse_pair(x)
                tmp.add(parse_pair(y))
                max_add = max(max_add, tmp.get_magnitude())

                tmp = parse_pair(y)
                tmp.add(parse_pair(x))
                max_add = max(max_add, tmp.get_magnitude())

        return max_add


if __name__ == '__main__':
    d18 = Day18()
    d18.main()
