from collections import defaultdict
from pprint import pprint


def get_my_input():
    raw_lines = open('input', 'r').readlines()
    return [(x.strip()) for x in raw_lines]


def main():
    docker = defaultdict(list)
    lines = get_my_input()

    # Building the docker
    for line in lines[:9]:
        line = f"{line: <35}"[1::4]
        for idx, i in enumerate(line, start=1):
            if i != ' ':
                docker[idx].insert(0, i)

    for idx, line in enumerate(lines[10:]):
        moves = line.split(' ')
        move_, from_, to_ = moves[1], moves[3], moves[5]

        # Part 1
        # for _ in range(int(move_)):
        #     box = docker[int(from_)].pop()
        #     docker[int(to_)].append(box)

        # Part 2
        boxes = docker[int(from_)][-int(move_):]
        docker[int(to_)].extend(boxes)
        docker[int(from_)] = docker[int(from_)][:-int(move_)]

    # SZVFSGCFG | VRQWPDSGP
    pprint(docker)
    print(*[docker[i][-1] for i in range(1, 10)], sep='')


if __name__ == '__main__':
    main()
