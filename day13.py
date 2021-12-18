from advent import AdventDay


def fold_points(points, fold):
    instr, v = fold
    axis = instr[-1]

    seen = set()
    new_points = []

    for x, y in points:
        if axis == 'x':
            x = v - abs(x - v)
        else:
            y = v - abs(y - v)

        if (x, y) not in seen:
            seen.add((x, y))
            new_points.append((x, y))

    return new_points


class Day13(AdventDay):

    def __init__(self):
        super().__init__(2021, 13)

    def part_1(self):
        points = self.split_types(',', (int, int))
        folds = self.split_types('=', (str, int))

        points = fold_points(points, folds[0])

        return len(points)
        
    def part_2(self):
        points = self.split_types(',', (int, int))
        folds = self.split_types('=', (str, int))

        for fold in folds:
            points = fold_points(points, fold)

        x_range = max(points, key=lambda v: v[0])[0]
        y_range = max(points, key=lambda v: v[1])[1]

        points = set(points)
        for y in range(y_range+1):
            for x in range(x_range+1):
                print('#' if (x, y) in points else ' ', end='')
            print('')
        print('\n')
        pass


if __name__ == '__main__':
    d13 = Day13()
    d13.main()
