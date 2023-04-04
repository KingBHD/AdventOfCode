from collections import defaultdict


def get_my_input():
    return open('input', 'r').read().splitlines()


class Day7:

    def __init__(self):
        self.tree = defaultdict(int)
        self.tree['/'] = 0
        self.pwd = []

    @property
    def at_path(self):
        return '/'.join(self.pwd)[1:] if len(self.pwd) > 1 else '/'

    def cd(self, _dir: str):
        if _dir == '..':
            self.pwd.pop()
        else:
            self.pwd.append(_dir)

    def mkdir(self, _name: str):
        if self.at_path[-1] == '/':
            new_path = self.at_path + _name
        else:
            new_path = self.at_path + '/' + _name
        self.tree[new_path] = self.tree[new_path] or 0

    def touch(self, _size: str, _name: str):
        self.tree[self.at_path] += int(_size)

    def calc_part_one(self):
        score = 0
        for __dir in self.tree.keys():
            temp = 0

            for __key, __value in self.tree.items():
                if __key.startswith(__dir):
                    temp += __value

            if temp <= 100000:
                score += temp
            self.tree[__dir] = temp

        print(f"Part 1: {score}")

    def calc_part_two(self):
        used_space = self.tree['/']
        free_space = 70000000 - used_space
        require_space = 30000000 - free_space

        # print("/", used_space)
        # print("Space Left", free_space)
        # print("Require", require_space)

        sorted_size = sorted(self.tree.values(), reverse=False)
        for size in sorted_size:
            if size > require_space:
                print("Part 2:", size)
                break


def main():
    day7 = Day7()
    for cmd in get_my_input():
        cmd = cmd.split(' ')
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                day7.cd(cmd[2])
            elif cmd[1] == 'ls':
                ...
        else:
            if cmd[0] == 'dir':
                day7.mkdir(cmd[1])
            else:
                day7.touch(*cmd)

    day7.calc_part_one()  # 1221521 | 1517599
    day7.calc_part_two()
    # pprint(day7.tree)


if __name__ == '__main__':
    main()
