from advent import AdventDay


class Day6(AdventDay):

    def __init__(self):
        super().__init__(2021, 6)

    def run_sim(self, steps):
        fish = self.parse_ints(one_per_line=True)
        fish_counts = [fish.count(i) for i in range(9)]

        for _ in range(steps):
            birth_count = fish_counts.pop(0)
            fish_counts[6] += birth_count
            fish_counts.append(birth_count)

        return sum(fish_counts)

    def part_1(self):
        return self.run_sim(80)

    def part_2(self):
        return self.run_sim(256)


if __name__ == '__main__':
    d6 = Day6()
    d6.main()
