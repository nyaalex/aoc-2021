from advent import AdventDay


class Day3(AdventDay):

    def __init__(self):
        super().__init__(2021, 3)

    def part_1(self):
        inp = self.read_line(bin)

        gamma = 0
        for i in range(12):
            bit = 1 << i
            count = 0
            for num in inp:
                count += ((num & bit) // bit) * 2 - 1

            gamma += bit * (0 if count < 0 else 1)

        epsilon = 0b111111111111 ^ gamma

        return gamma * epsilon

    def part_2(self):
        inp = self.read_line(bin)
        co2 = inp.copy()
        oxygen = inp.copy()

        # Calculate co2 first
        bit = 1 << 11
        while len(oxygen) > 1:
            c = 0
            for i in oxygen:
                c += ((i & bit)//bit)*2 - 1

            most_common = 0 if c < 0 else 1
            oxygen = [i for i in oxygen if (i & bit) == (most_common * bit)]
            bit >>= 1

        # Calculate co2 first
        bit = 1 << 11
        while len(co2) > 1:
            c = 0
            for i in co2:
                c += ((i & bit)//bit) * 2 - 1

            least_common = 1 if c < 0 else 0
            co2 = [i for i in co2 if (i & bit) == (least_common * bit)]
            bit >>= 1

        return co2[0] * oxygen[0]


if __name__ == '__main__':
    d3 = Day3()
    d3.main()
