from advent import AdventDay


class Day14(AdventDay):

    def __init__(self):
        super().__init__(2021, 14)

    def get_rule(self):
        rules = self.split_types(' -> ', (str, str))
        rule_lookup = {}

        for pair, insert in rules:
            a, b = pair
            rule_lookup[pair] = (a+insert, insert+b)

        return rule_lookup

    @staticmethod
    def apply_rule(rule, polymer):
        new_polymer = {}
        for pair, count in polymer.items():
            a, b = rule[pair]

            if a in new_polymer:
                new_polymer[a] += count
            else:
                new_polymer[a] = count

            if b in new_polymer:
                new_polymer[b] += count
            else:
                new_polymer[b] = count

        return new_polymer

    def get_polymer(self):
        polymer = self.read_lines()[0]
        polymer_table = {}

        for i in range(len(polymer) - 1):
            pair = polymer[i:i+2]
            if pair in polymer_table:
                polymer_table[pair] += 1
            else:
                polymer_table[pair] = 1

        return polymer[0], polymer_table

    @staticmethod
    def get_result(polymer, first):
        total = {first: 1}
        for pair, count in polymer.items():
            a, b = pair

            if b in total:
                total[b] += count
            else:
                total[b] = count

        most_common = max(total.items(), key=lambda x: x[1])[1]
        least_common = min(total.items(), key=lambda x: x[1])[1]

        return most_common - least_common

    def part_1(self):
        first, polymer = self.get_polymer()
        rule = self.get_rule()

        for i in range(10):
            polymer = self.apply_rule(rule, polymer)

        return self.get_result(polymer, first)

    def part_2(self):
        first, polymer = self.get_polymer()
        rule = self.get_rule()

        for i in range(40):
            polymer = self.apply_rule(rule, polymer)

        return self.get_result(polymer, first)


if __name__ == '__main__':
    d14 = Day14()
    d14.main()
