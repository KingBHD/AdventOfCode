def get_my_input():
    return open('input', 'r').read().splitlines()


class Day6:

    def __init__(self):
        self.sidx = 0
        self.eidx = 4

    def has_duplicate(self, string: str):
        if len(set(string)) != 4:
            self.sidx += 1
            self.eidx += 1
            return True
        return False

    def main(self):
        line = get_my_input()[0]

        print([(self.eidx, line[self.sidx:self.eidx]) for _ in line
               if not self.has_duplicate(line[self.sidx:self.eidx])][0][0])


if __name__ == '__main__':
    day = Day6()
    day.main()
