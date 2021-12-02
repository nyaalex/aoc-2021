from advent import AdventDay


class Day2(AdventDay):

    def __init__(self):
        super().__init__(2)

    def part_1(self):
        inp = self.split_types(types=(str, int))

        x = 0
        y = 0

        for direction, value in inp:
            if direction == 'forward':
                x += value
            elif direction == 'up':
                y -= value
            else:
                y += value

        return x*y

    def part_2(self):
        inp = self.split_types(types=(str, int))

        x = 0
        aim = 0
        y = 0

        for direction, value in inp:
            if direction == 'forward':
                x += value
                y += aim * value
            elif direction == 'up':
                aim -= value
            else:
                aim += value

        return x * y


if __name__ == '__main__':
    d2 = Day2()
    d2.main()
