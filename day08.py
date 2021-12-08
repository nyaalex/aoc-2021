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
        code = [0 for _ in range(10)]

        for i in int_codes:
            if Day8.count_bits(i) == 2:
                code[1] = i
            elif Day8.count_bits(i) == 3:
                code[7] = i
            elif Day8.count_bits(i) == 4:
                code[4] = i
            elif Day8.count_bits(i) == 7:
                code[8] = i

        # 4 down, 6 to go
        # I'd like to make the note here that every one of these rules was worked out by hand, this will decode
        # accurately but the precise reasoning why is specific per number, and I cba to explain
        for i in int_codes:
            if Day8.count_bits(i) == 5:
                if i & code[1] == code[1]:
                    code[3] = i
                elif Day8.count_bits(i ^ code[4]) == 5:
                    code[2] = i
                else:
                    code[5] = i
            elif Day8.count_bits(i) == 6:
                if Day8.count_bits(i ^ code[1]) == 6:
                    code[6] = i
                elif Day8.count_bits(i ^ code[4]) == 4:
                    code[0] = i
                else:
                    code[9] = i

        return dict([(v, i) for i, v in enumerate(code)])

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

            decoded_number = 0
            for i in encoded.split():
                decoded_number *= 10
                code = self.convert_to_int(i)
                val = true_encoding[code]
                decoded_number += val

            total += decoded_number

        return total


if __name__ == '__main__':
    d8 = Day8()
    d8.main()
