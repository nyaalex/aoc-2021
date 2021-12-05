from advent import AdventDay


class Day5(AdventDay):

    def __init__(self):
        super().__init__(2021, 5)

    def find_intersections(self, ignore_diagonals):
        inp = self.parse_ints()
        seen = set()
        intersection = set()

        for x1, y1, x2, y2 in inp:

            if x1 != x2 and y1 != y2 and ignore_diagonals:
                continue

            dx = x2 - x1
            x_sign = min(1, max(dx, -1))
            x_distance = abs(dx)

            dy = y2 - y1
            y_sign = min(1, max(dy, -1))
            y_distance = abs(dy)

            line_range = ((x1 + i * x_sign, y1 + i * y_sign) for i in range(max(x_distance, y_distance) + 1))

            for coord in line_range:
                if coord in seen:
                    intersection.add(coord)
                else:
                    seen.add(coord)

        return len(intersection)

    def part_1(self):
        return self.find_intersections(ignore_diagonals=True)

        
    def part_2(self):
        return self.find_intersections(ignore_diagonals=False)


if __name__ == '__main__':
    d5 = Day5()
    d5.main()
