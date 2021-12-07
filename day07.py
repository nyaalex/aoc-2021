from advent import AdventDay


class Day7(AdventDay):

    def __init__(self):
        super().__init__(2021, 7)

    def solve(self, part):
        crabs = self.parse_ints(True)

        lowest_fuel_count = float('inf')
        for dist in range(max(crabs)):
            fuel = 0
            for crab in crabs:
                to_move = abs(crab - dist)

                if part == 1:
                    fuel += to_move
                else:
                    fuel += (to_move * (to_move + 1)) // 2

            if fuel < lowest_fuel_count:
                lowest_fuel_count = fuel
        return lowest_fuel_count

    def part_1(self):
        return self.solve(part=1)

    def part_2(self):
        return self.solve(part=2)


if __name__ == '__main__':
    d7 = Day7()
    d7.main()
