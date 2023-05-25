from asyncio import Queue
from collections import defaultdict
from string import ascii_lowercase


class Day12:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.heightmap = []
        self.start = ()
        self.end = ()

    @staticmethod
    def get_inputs():
        with open('input', 'r') as f:
            return f.read().splitlines()

    def read_heightmap(self):
        for idx, row in enumerate(self.get_inputs()):
            my_row = []
            for idy, char in enumerate(row):
                if char not in ['S', 'E']:
                    char = ascii_lowercase.index(char) + 1

                if char == 'S':
                    char = 1
                    self.start = (idx, idy)

                if char == 'E':
                    char = 26
                    self.end = (idx, idy)

                my_row.append(char)
            self.heightmap.append(my_row)

    def get_adjacency_list(self):
        for idx, row in enumerate(self.heightmap):
            for idy, _ in enumerate(row):
                candidates = []
                row_value = self.heightmap[idx][idy]
                nears = self.get_neighbours(idx, idy)
                for n in nears:
                    new_value = self.heightmap[n[0]][n[1]]
                    if row_value == new_value - 1 or row_value <= new_value:
                        candidates.append(n)

                self.adjacency_list[(idx, idy)] = candidates

    def get_neighbours(self, x, y):
        neighbours = []
        if x > 0:
            neighbours.append((x - 1, y))
        if x < len(self.heightmap) - 1:
            neighbours.append((x + 1, y))
        if y > 0:
            neighbours.append((x, y - 1))
        if y < len(self.heightmap[0]) - 1:
            neighbours.append((x, y + 1))
        return neighbours

    def get_bfs(self, start):
        visited = [start]
        q = Queue()
        q.put_nowait(start)

        while not q.empty():
            node = q.get_nowait()
            neighbours = self.adjacency_list[node]

            for _next in neighbours:
                if _next not in visited:
                    q.put_nowait(_next)
                    visited.append(_next)

                    if _next == self.end:
                        return True

        return False


day12 = Day12()
day12.read_heightmap()
day12.get_adjacency_list()
prev = day12.get_bfs(day12.start)
# print(prev)

print(len(prev[prev.index(day12.start):prev.index(day12.end)]))

# day12.get_path()
#
# with open('output3', 'w') as f:
#     for o, p in enumerate(prev):
#         day12.heightmap[p[0]][p[1]] = '.'
#
#     # for key, value in day12.adjacency_list.items():
#     # f.write(f"{key} -> {', '.join(map(str, value)) or 'null'}")
#     # f.write("\n")
#
#     for rzow in day12.heightmap:
#         f.write(''.join(f"{x}" for x in rzow))
#         f.write('\n')
