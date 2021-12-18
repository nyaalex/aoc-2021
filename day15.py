from advent import AdventDay
from queue import PriorityQueue


def get_path(graph, part):

    start = (0, 0)

    max_x = len(graph)
    max_y = len(graph[0])

    if part == 1:
        size = (max_x - 1, max_y - 1)
    else:
        size = (5 * max_x - 1, 5 * max_y - 1)
        true_size = (max_x, max_y)
    end = size

    open_set = {start}
    open_queue = PriorityQueue()
    open_queue.put((0, start))

    known_score = {start: 0}

    while open_set:
        current = open_queue.get()[1]
        open_set.remove(current)

        if current == end:
            return known_score[current]

        for neighbour in AdventDay.get_neighbours(current, size, von_neumann=True):
            n_x, n_y = neighbour

            if part == 1:
                weight = graph[n_x][n_y]
            else:
                # Find which large square we are in, and from that the modifier
                b_x = n_x // true_size[0]
                b_y = n_y // true_size[1]
                mod = b_x + b_y

                # Find where we are in that square, and from that the original weight
                s_x = n_x % true_size[0]
                s_y = n_y % true_size[1]
                weight = graph[s_x][s_y]

                weight = (((weight + mod) - 1) % 9) + 1

            new_score = weight + known_score[current]

            if neighbour not in known_score:
                known_score[neighbour] = float('inf')

            if new_score < known_score[neighbour]:
                known_score[neighbour] = new_score
                guessed_score = known_score[neighbour] + abs((end[0] - n_x) + (end[1] - n_y))

                if neighbour not in open_set:
                    open_set.add(neighbour)
                    open_queue.put((guessed_score, neighbour))
    return False


class Day15(AdventDay):

    def __init__(self):
        super().__init__(2021, 15)

    def part_1(self):
        risk_map = self.int_grid()

        return get_path(risk_map, part=1)
        
    def part_2(self):
        risk_map = self.int_grid()

        return get_path(risk_map, part=2)


if __name__ == '__main__':
    d15 = Day15()
    d15.main()
