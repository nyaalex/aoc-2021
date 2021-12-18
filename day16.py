from advent import AdventDay


def product(arr):
    c = 1
    for i in arr:
        c *= i
    return c


class PacketParser:

    function_map = [
        sum,
        product,
        min,
        max,
        None,
        lambda a: 1 if a[0] > a[1] else 0,
        lambda a: 1 if a[0] < a[1] else 0,
        lambda a: 1 if a[0] == a[1] else 0,
    ]

    def __init__(self, packet):
        self.packet = list(packet)
        self.buffer = 0
        self.pointer = -1
        self.bits_read = 0

    def read_bits(self, bits):
        self.bits_read += bits

        while self.pointer < (bits - 1):
            self.buffer <<= 4
            self.pointer += 4
            self.buffer += int(self.packet.pop(0), 16)

        c = 0
        for _ in range(bits):
            c <<= 1
            c += 1 if self.buffer & (1 << self.pointer) else 0
            self.buffer &= ~(1 << self.pointer)
            self.pointer -= 1

        return c

    def parse_literal(self):
        data = 0
        should_read = 1
        while should_read:
            should_read = self.read_bits(1)
            data <<= 4
            data += self.read_bits(4)

        return data

    def parse(self):
        version = self.read_bits(3)
        packet_type = self.read_bits(3)

        if packet_type == 4:
            data = self.parse_literal()
            return version, packet_type, data
        else:
            sub_packets = self.parse_operator()
            return version, packet_type, sub_packets

    def parse_operator(self):
        length_id = self.read_bits(1)

        sub_packets = []
        if length_id:
            num_packets = self.read_bits(11)
            while len(sub_packets) < num_packets:
                sub_packets.append(self.parse())

        else:
            bit_length = self.read_bits(15)
            read_to = self.bits_read + bit_length
            while self.bits_read < read_to:
                sub_packets.append(self.parse())

        return sub_packets

    @staticmethod
    def total_versions(packet):
        version, packet_type, data = packet

        if packet_type == 4:
            return version

        for sub_packet in data:
            version += PacketParser.total_versions(sub_packet)

        return version

    @staticmethod
    def execute_packet(packet):
        version, packet_type, data = packet

        operation = PacketParser.function_map[packet_type]

        if packet_type == 4:
            return data

        else:
            sub_values = [PacketParser.execute_packet(sub_packet) for sub_packet in data]
            return operation(sub_values)


class Day16(AdventDay):

    def __init__(self):
        super().__init__(2021, 16)

    def part_1(self):
        encoded_packet = self.day_input
        parser = PacketParser(encoded_packet)
        packet = parser.parse()

        return parser.total_versions(packet)

    def part_2(self):
        encoded_packet = self.day_input
        parser = PacketParser(encoded_packet)
        packet = parser.parse()

        return parser.execute_packet(packet)


if __name__ == '__main__':
    d16 = Day16()
    d16.main()
