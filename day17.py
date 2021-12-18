from advent import AdventDay


class Day17(AdventDay):

    def __init__(self):
        super().__init__(2021, 17)

    @staticmethod
    def hits(v, box):
        x_min, x_max, y_min, y_max = box
        x_v, y_v = v
        x, y = 0, 0

        while True:
            if x > x_max or y < y_min:
                return False
            elif x >= x_min and y <= y_max:
                return True
            x += x_v
            y += y_v

            y_v -= 1
            x_v -= min(max(-1, x_v), 1)

    def part_1(self):
        box = self.parse_ints(one_per_line=True)
        x_min, x_max, y_min, y_max = box

        return (y_min * (y_min + 1))//2

    def part_2(self):
        box = self.parse_ints(one_per_line=True)
        x_min, x_max, y_min, y_max = box

        xv_min = int((2 * x_min)**0.5) - 1
        xv_max = x_max + 1

        yv_min = y_min
        yv_max = - y_min

        total = 0
        for y in range(yv_min, yv_max):
            for x in range(xv_min, xv_max):
                total += 1 if self.hits((x, y), box) else 0

        return total


if __name__ == '__main__':
    d17 = Day17()
    d17.main()
