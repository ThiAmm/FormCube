import itertools
import numpy as np
from list_rotations import list_rotations


def get_combinations(coordinate_system, point_to_reference_corner_of_cube, cube_parts, shape, dimension):
    combinations = [coordinate_system]
    for cube_part in cube_parts:
        combinations_new = []
        for combination in combinations:
            for index in itertools.product(*[range(0, n) for n in shape]):
                position_in_cube = np.add(point_to_reference_corner_of_cube, np.array(index))
                cube_part_in_reference_array = np.zeros(coordinate_system.shape)
                cube_part_in_reference_array[(slice(position_in_cube[0], position_in_cube[0] + cube_part.shape[0]),
                                              slice(position_in_cube[1], position_in_cube[1] + cube_part.shape[1]),
                                              slice(position_in_cube[2], position_in_cube[2] + cube_part.shape[2]))] \
                    += cube_part
                for rotated_cube_part in list_rotations(cube_part_in_reference_array, dimension):
                    combination_with_rotated_cube_part = combination + rotated_cube_part
                    combinations_new.append(combination_with_rotated_cube_part)
        combinations = combinations_new

    return combinations
