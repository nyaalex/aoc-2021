from advent import AdventDay


def part1_algorithm(graph, seen=None, cave='start', extra_visit=False):
    if seen is None:
        seen = {'start'}

    total = 0
    for n in graph[cave]:

        if n == 'start':
            continue

        elif n == 'end':
            total += 1

        elif n.islower():
            if extra_visit and n in seen:
                total += part1_algorithm(graph, {n} | seen, n, False)

            elif n not in seen:
                total += part1_algorithm(graph, {n} | seen, n, extra_visit)

        elif n.isupper():
            total += part1_algorithm(graph, seen, n, extra_visit)

    return total


class Day12(AdventDay):

    def __init__(self):
        super().__init__(2021, 12)

    def build_graph(self):
        inp = self.split_types('-', (str, str))

        graph = {}
        for s, e in inp:
            if s not in graph:
                graph[s] = []
            if e not in graph:
                graph[e] = []

            graph[s].append(e)
            graph[e].append(s)

        return graph

    def part_1(self):
        graph = self.build_graph()

        result = part1_algorithm(graph)
        return result

    def part_2(self):
        graph = self.build_graph()

        result = part1_algorithm(graph, extra_visit=True)
        return result


if __name__ == '__main__':
    d12 = Day12()
    d12.main()
