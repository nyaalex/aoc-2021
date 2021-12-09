from advent import AdventDay


class Day9(AdventDay):

    def __init__(self):
        super().__init__(2021, 9)

    def get_low_points(self, heightmap):
        max_x = len(heightmap)
        max_y = len(heightmap[0])
        low_points = []

        for x in range(max_x):
            for y in range(max_y):
                v = heightmap[x][y]

                n = []
                for d_x, d_y in self.v_neighbours:
                    n_x, n_y = x + d_x, y + d_y
                    if 0 <= n_x < max_x and 0 <= n_y < max_y:
                        n.append(heightmap[n_x][n_y])

                if all([v < i for i in n]):
                    low_points.append(((x, y), v))

        return low_points

    def get_basin_size(self, heightmap, node):
        max_x = len(heightmap)
        max_y = len(heightmap[0])
        seen = set()
        stack = [None]

        while node is not None:
            seen.add(node)
            x, y = node

            n = []
            for d_x, d_y in self.v_neighbours:
                n_x, n_y = x + d_x, y + d_y
                if 0 <= n_x < max_x and 0 <= n_y < max_y:
                    if (n_x, n_y) not in seen and heightmap[n_x][n_y] != 9:
                        n.append((n_x, n_y))

            if n:
                stack.append(node)
                node = n[0]
            else:
                node = stack.pop()

        return len(seen)

    def part_1(self):
        inp = self.read_lines()
        heightmap = [[int(i) for i in line] for line in inp]

        l_points = self.get_low_points(heightmap)

        total = 0
        for _, v in l_points:
            total += v+1

        return total

    def part_2(self):
        inp = self.read_lines()
        heightmap = [[int(i) for i in line] for line in inp]

        l_points = self.get_low_points(heightmap)
        basin_sizes = []

        for start, _ in l_points:
            size = self.get_basin_size(heightmap, start)
            basin_sizes.append(size)

        top3 = sorted(basin_sizes)[-3:]
        return top3[0] * top3[1] * top3[2]


if __name__ == '__main__':
    d9 = Day9()
    d9.main()
