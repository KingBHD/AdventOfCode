def get_inputs():
    with open('input', 'r') as f:
        return f.read().splitlines()


def main():
    visible, not_visible, scenic_score = 0, 0, 0
    lines = get_inputs()
    grid = [list(map(int, line)) for line in lines]

    # pprint(grid)
    for outer_idx, row in enumerate(grid):
        if outer_idx in [0, len(grid) - 1]:
            visible += len(row)
            continue

        enclosed_trees = row[1:-1]
        visible += 2

        for inner_idx, tree in enumerate(enclosed_trees):
            right_trees = row[inner_idx + 2:]
            left_trees = row[:inner_idx + 1]

            top_trees = [tops[inner_idx + 1] for tops in grid[:outer_idx]]
            bottom_trees = [bottoms[inner_idx + 1] for bottoms in grid[outer_idx + 1:]]

            # print([top_trees, left_trees, tree, right_trees, bottom_trees])

            # Part 1
            top = [__t >= tree for __t in top_trees]
            left = [__l >= tree for __l in left_trees]
            right = [__r >= tree for __r in right_trees]
            bottom = [__b >= tree for __b in bottom_trees]

            if any(top) and any(left) and any(right) and any(bottom):
                not_visible += 1
            else:
                visible += 1

            # Part 2
            top_scenic_score = 0
            for __t in reversed(top_trees):
                top_scenic_score += 1
                if tree <= __t:
                    break

            left_scenic_score = 0
            for __l in reversed(left_trees):
                left_scenic_score += 1
                if tree <= __l:
                    break

            right_scenic_score = 0
            for __r in right_trees:
                right_scenic_score += 1
                if tree <= __r:
                    break

            bottom_scenic_score = 0
            for __b in bottom_trees:
                bottom_scenic_score += 1
                if tree <= __b:
                    break

            tree_scenic_score = top_scenic_score * left_scenic_score * right_scenic_score * bottom_scenic_score
            # print(f"{tree = }", top_scenic_score, left_scenic_score, right_scenic_score, bottom_scenic_score)
            # print(f"Scenic Score {tree}:", tree_scenic_score)
            scenic_score = max([tree_scenic_score, scenic_score])

    print("Visible:", visible)
    print("Not Visible:", not_visible)
    print("Best Scenic Score:", scenic_score)  # 882816


if __name__ == '__main__':
    main()
