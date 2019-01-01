def test():
    import numpy as np

    cube_part1 = np.array(
        [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])
    cube_part2 = np.ones((3, 3, 3)) - cube_part1
    print(len(list_combinations([cube_part1, cube_part2], [3, 3, 3])))


test()