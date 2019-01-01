def test_list_rotations():
    from list_rotations import list_rotations
    import numpy as np

    cube_part1 = np.array(
        [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])
    list_rotations(cube_part1)

test_list_rotations()
