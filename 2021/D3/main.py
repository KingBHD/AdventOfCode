def get_my_input():
    raw_lines = open('input', 'r').readlines()
    return raw_lines


def main():
    gamma_rate = []
    epsilon_rate = []
    binaries = get_my_input()
    i = 0
    while i != (len(binaries[0]) - 1):
        zero = 0
        one = 0
        for binary in binaries:
            if binary[i] == '1':
                one += 1
            else:
                zero += 1

        if zero > one:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        i += 1

    print(int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2))


if __name__ == '__main__':
    main()
