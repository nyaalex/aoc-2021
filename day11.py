from advent import AdventDay


class OctoGrid:

    def __init__(self, inp_grid):
        self.main_grid = inp_grid
        self.shape = (len(inp_grid) - 1, len(inp_grid[0]) - 1)

        self.flashes = 0

    def update(self):
        should_flash = []
        # increment every member of the grid
        for x in range(self.shape[0] + 1):
            for y in range(self.shape[1] + 1):

                self.main_grid[x][y] += 1

                if self.main_grid[x][y] > 9:
                    should_flash.append((x, y))
                    self.main_grid[x][y] = 0

        # flash
        while should_flash:
            flash_octo = should_flash.pop()
            self.flashes += 1

            for nx, ny in AdventDay.get_neighbours(flash_octo, self.shape):
                n_octo = self.main_grid[nx][ny]

                if n_octo == 0:
                    continue
                elif n_octo < 9:
                    self.main_grid[nx][ny] += 1
                elif n_octo == 9:
                    should_flash.append((nx, ny))
                    self.main_grid[nx][ny] = 0


class Day11(AdventDay):

    def __init__(self):
        super().__init__(2021, 11)

    def part_1(self):
        inp = self.int_grid()
        octopi = OctoGrid(inp)

        for _ in range(100):
            octopi.update()

        return octopi.flashes

    def part_2(self):
        inp = self.int_grid()
        octopi = OctoGrid(inp)

        turn_count = 0
        flash_count = 0
        while flash_count != 100:
            turn_count += 1
            octopi.update()
            flash_count = octopi.flashes
            octopi.flashes = 0

        return turn_count


if __name__ == '__main__':
    d11 = Day11()
    d11.main()
