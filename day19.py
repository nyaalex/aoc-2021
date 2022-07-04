from advent import AdventDay


class Scanner:
    INTERSECTION_THRESHOLD = 12

    def __init__(self, scanner_id):
        self.scanner_id = scanner_id
        self.beacons = []
        self.added = {scanner_id}
        self.positions = [(scanner_id, (0, 0, 0))]

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

    @staticmethod
    def apply_transformation(rotation, translation, beacon):
        x, y, z = beacon
        ((a, b, c),
         (d, e, f),
         (g, h, i)) = rotation
        s_x, s_y, s_z = translation

        n_x = a * x + b * y + c * z + s_x
        n_y = d * x + e * y + f * z + s_y
        n_z = g * x + h * y + i * z + s_z

        return n_x, n_y, n_z

    @staticmethod
    def find_transformation(intersections):
        rotation = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
        translation = [0, 0, 0]
        for axis in range(3):
            max_count = 0
            for a, b, c in [
                (1, 0, 0), (-1, 0, 0),
                (0, 1, 0), (0, -1, 0),
                (0, 0, 1), (0, 0, -1),
            ]:
                if axis == 1:
                    ((i, ii, iii), (_, _, _), (_, _, _)) = rotation
                    if abs(a * i) or abs(b * ii) or abs(c * iii):
                        continue

                if axis == 2:
                    ((i, ii, iii), (d, e, f), (_, _, _)) = rotation
                    if (a, b, c) != (ii * f - iii * e, iii * d - i * f, i * e - ii * d):
                        continue

                counter = dict()

                for v, (x2, y2, z2) in intersections:
                    potential_value = v[axis] - a * x2 - b * y2 - c * z2
                    if potential_value not in counter:
                        counter[potential_value] = 0
                    counter[potential_value] += 1

                best_guess, current_count = max(counter.items(), key=lambda _: _[1])
                if current_count > max_count:
                    translation[axis] = best_guess
                    rotation[axis] = (a, b, c)
                    max_count = current_count

            if max_count < Scanner.INTERSECTION_THRESHOLD:
                return None, None

        return rotation, translation

    def find_intersections(self, alt_scanner: 'Scanner'):
        intersections = []

        for beacon_a in self.beacons:
            for beacon_b in alt_scanner.beacons:
                intersections.append((beacon_a, beacon_b))

        rotation, translation = self.find_transformation(intersections)
        if rotation is None:
            return []

        true_intersections = []
        for a, b in intersections:
            if self.apply_transformation(rotation, translation, b) == a:
                true_intersections.append((a, b))

        return true_intersections

    def combine_scanner(self, alt_scanner: 'Scanner'):
        if alt_scanner.scanner_id in self.added:
            return 0

        intersections = self.find_intersections(alt_scanner)
        if len(intersections) < Scanner.INTERSECTION_THRESHOLD:
            return 0

        _, alt_intersecting = zip(*intersections)
        alt_intersecting = set(alt_intersecting)
        rotation, translation = self.find_transformation(intersections)
        added = 0
        for beacon in alt_scanner.beacons:
            if beacon in alt_intersecting:
                continue

            beacon = self.apply_transformation(rotation, translation, beacon)
            if beacon in self.beacons:
                continue
            self.add_beacon(beacon)
            added += 1

        for scanner_id, position in alt_scanner.positions:
            if scanner_id not in self.added:
                self.positions.append((scanner_id, self.apply_transformation(rotation, translation, position)))

        self.added.update(alt_scanner.added)
        return added


class Day19(AdventDay):

    def __init__(self):
        super().__init__(2021, 19)
        self.scanner_0 = None

    def part_1(self):
        scanners = []

        for line in self.parse_ints():
            if len(line) == 1:
                scanners.append(Scanner(line[0]))
            else:
                scanners[-1].add_beacon(tuple(line))

        self.scanner_0 = scanners.pop(0)
        added_this_round = 1
        while added_this_round != 0:
            added_this_round = 0
            for scanner in scanners:
                added_this_round += self.scanner_0.combine_scanner(scanner)

        failed = False
        for scanner in scanners:
            if scanner.scanner_id not in self.scanner_0.added:
                failed = True
                print("Never added scanner %s, not enough intersections found" % scanner.scanner_id)

        if failed:
            return -1

        return len(self.scanner_0.beacons)

    def part_2(self):
        max_dist = 0
        for _, pos_a in self.scanner_0.positions:
            for _, pos_b in self.scanner_0.positions:
                dist = self.distance(pos_a, pos_b)
                if dist > max_dist:
                    max_dist = dist

        return max_dist


if __name__ == '__main__':
    d19 = Day19()
    d19.main()
