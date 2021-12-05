from advent import AdventDay


class Day5(AdventDay):

    def __init__(self):
        super().__init__(2021, 5)

    def part_1(self):
        inp = self.parse_ints()
        seen = set()
        intersection = set()

        for x1, y1, x2, y2 in inp:

            if x1 == x2:
                start = min(y1, y2)
                end = y1+y2 - start
                line_range = ((x1, i) for i in range(start, end+1))
            elif y1 == y2:
                start = min(x1, x2)
                end = x1+x2 - start
                line_range = ((i, y1) for i in range(start, end+1))
            else:
                continue

            for coord in line_range:
                if coord in seen:
                    intersection.add(coord)
                else:
                    seen.add(coord)

        return len(intersection)
        
    def part_2(self):
        inp = self.parse_ints()
        seen = set()
        intersection = set()

        for x1, y1, x2, y2 in inp:

            if x1 == x2:
                start = min(y1, y2)
                end = y1+y2 - start
                line_range = ((x1, i) for i in range(start, end+1))
            elif y1 == y2:
                start = min(x1, x2)
                end = x1+x2 - start
                line_range = ((i, y1) for i in range(start, end+1))
            else:
                top_x, top_y = min((x1, y1), (x2, y2), key=lambda x: x[1])
                bottom_x = x1+x2 - top_x
                dx = bottom_x - top_x

                sign = -1 if dx < 0 else 1
                distance = abs(dx)

                line_range = ((top_x + sign * i, top_y + i) for i in range(distance+1))

            for coord in line_range:
                if coord in seen:
                    intersection.add(coord)
                else:
                    seen.add(coord)

        return len(intersection)


if __name__ == '__main__':
    d5 = Day5()
    d5.main()
