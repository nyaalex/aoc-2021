from advent import AdventDay


class Day10(AdventDay):

    def __init__(self):
        super().__init__(2021, 10)

    def part_1(self):
        inp = self.read_lines()

        invalid_lookup = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        valid_lookup = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>',
        }
        total = 0
        for line in inp:
            stack = []
            for c in line:
                if c in valid_lookup:
                    stack.append(c)
                else:
                    opener = stack.pop()
                    if c != valid_lookup[opener]:
                        total += invalid_lookup[c]
                        break

        return total

    def part_2(self):
        inp = self.read_lines()

        score_lookup = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4
        }
        valid_lookup = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>',
        }
        all_scores = []
        for line in inp:
            stack = []
            for c in line:
                if c in '([{<':
                    stack.append(c)
                else:
                    opener = stack.pop()
                    if c != valid_lookup[opener]:
                        stack = []
                        break
            # Calculate line score
            score = 0
            for c in stack[::-1]:
                score *= 5
                score += score_lookup[c]

            if score:
                all_scores.append(score)

        all_scores.sort()
        median = all_scores[len(all_scores)//2]

        return median


if __name__ == '__main__':
    d10 = Day10()
    d10.main()
