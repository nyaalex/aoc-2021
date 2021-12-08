from advent import AdventDay


class Day8(AdventDay):

    def __init__(self):
        super().__init__(2021, 8)

    @staticmethod
    def convert_to_int(code):
        tot = 0
        for c in code:
            tot += 1 << (ord(c) - 97)
        return tot

    @staticmethod
    def count_bits(num):
        tot = 0
        for i in range(num.bit_length()):
            tot += 1 if num & 1 << i else 0
        return tot

    @staticmethod
    def decode(int_codes):
        vals = [0 for _ in range(10)]

        for i in int_codes:
            if Day8.count_bits(i) == 2:
                vals[1] = i
            elif Day8.count_bits(i) == 3:
                vals[7] = i
            elif Day8.count_bits(i) == 4:
                vals[4] = i
            elif Day8.count_bits(i) == 7:
                vals[8] = i

        # 4 down, 6 to go
        # I'd like to make the note here that every one of these rules was worked out by hand, this will decode
        # accurately but the reason why is that it just does
        for i in int_codes:
            if Day8.count_bits(i) == 5:
                if i & vals[1] == vals[1]:
                    vals[3] = i
                elif Day8.count_bits(i ^ vals[4]) == 5:
                    vals[2] = i
                else:
                    vals[5] = i
            elif Day8.count_bits(i) == 6:
                if Day8.count_bits(i ^ vals[1]) == 6:
                    vals[6] = i
                elif Day8.count_bits(i ^ vals[4]) == 4:
                    vals[0] = i
                else:
                    vals[9] = i

        final_lookup = dict([(v, i) for i, v in enumerate(vals)])
        return final_lookup

    def part_1(self):
        inp = self.split_types(delim=' | ', types=(str, str))
        total = 0
        for encoding, encoded in inp:
            for i in encoded.split():
                if len(i) in (2, 3, 4, 7):
                    total += 1

        return total
        
    def part_2(self):
        inp = self.split_types(delim=' | ', types=(str, str))
        total = 0

        for encoding, encoded in inp:
            int_code = [self.convert_to_int(i) for i in encoding.split()]
            true_encoding = self.decode(int_code)

            v = 0
            for i in encoded.split():
                v *= 10
                code = self.convert_to_int(i)
                val = true_encoding[code]
                v += val

            total += v

        return total


if __name__ == '__main__':
    d8 = Day8()
    d8.main()
