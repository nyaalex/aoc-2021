from advent import AdventDay


class Day1(AdventDay):

    def __init__(self):
        super().__init__(1)

    def part_1(self):
        inp = self.parse_ints(one_per_line=True)
        count = 0

        for i in range(1, len(inp)):
            count += inp[i] > inp[i-1]

        return count

    def part_2(self):
        inp = self.parse_ints(one_per_line=True)
        count = 0

        for i in range(3, len(inp)):
            count += sum(inp[i-3:i]) > sum(inp[i-4:i-1])

        return count


if __name__ == '__main__':
    d1 = Day1()
    d1.main()
