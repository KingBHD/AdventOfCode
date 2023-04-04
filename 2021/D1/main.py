def get_my_input():
    raw_lines = open('input', 'r').readlines()
    return [int(x.strip()) for x in raw_lines]


def part_one():
    count = 0
    lines = get_my_input()
    for idx, current_line in enumerate(lines):
        if idx == 0:
            print('N/A - no previous measurement')
            continue
        if current_line > lines[idx - 1]:
            count += 1
            print('increased')
        else:
            print('decreased')
    print(count)


def max_sum_fn(arr, k):
    count = 0
    n = len(arr)

    if n < k:
        print("Invalid")
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum
    print(f'{window_sum} (N/A - no previous sum)')

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        if max_sum < window_sum:
            print(f'{window_sum} (increased)')
            count = count + 1
        elif max_sum > window_sum:
            print(f'{window_sum} (decreased)')
        else:
            print(f'{window_sum} (no change)')
        max_sum = window_sum

        # max_sum = max(window_sum, max_sum)
    print("Total increased: ", count)


def part_two():
    lines = get_my_input()
    max_sum_fn(lines, 3)


def main():
    part_two()


if __name__ == '__main__':
    main()
