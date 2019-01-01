def list_combinations(cube_parts, shape, dimension=3):
    from list_rotations import list_rotations
    import numpy as np
    import itertools
    import math

    shapes_of_cube_parts = map(np.shape, cube_parts)
    maximal_length_of_cube_part = max(max(shape_of_cube_part) for shape_of_cube_part in shapes_of_cube_parts)
    point_to_reference_corner_of_cube = [maximal_length_of_cube_part]*dimension
    length_in_all_dimensions = max(shape) + maximal_length_of_cube_part*2
    reference_array = np.zeros([length_in_all_dimensions]*dimension)

    combinations = [reference_array]
    for cube_part in cube_parts:
        combinations_new = []
        for combination in combinations:
            for index in itertools.product(*[range(0, n) for n in shape]):
                position_in_cube = np.add(point_to_reference_corner_of_cube, np.array(index))
                cube_part_in_reference_array = np.zeros(reference_array.shape)
                cube_part_in_reference_array[(slice(position_in_cube[0], position_in_cube[0]+cube_part.shape[0]),
                                 slice(position_in_cube[1], position_in_cube[1] + cube_part.shape[1]),
                                 slice(position_in_cube[2], position_in_cube[2] + cube_part.shape[2]))]\
                    += cube_part
                for rotated_cube_part in list_rotations(cube_part_in_reference_array, dimension):
                    combination_with_rotated_cube_part = combination + rotated_cube_part
                    combinations_new.append(combination_with_rotated_cube_part)
        combinations = combinations_new

    desired_object_from_cube_parts = np.zeros(reference_array.shape)
    desired_object_from_cube_parts[(slice(point_to_reference_corner_of_cube[0],
                                          point_to_reference_corner_of_cube[0]+max(shape)
                                          ),
                                    slice(point_to_reference_corner_of_cube[1],
                                          point_to_reference_corner_of_cube[1] + max(shape)
                                          ),
                                    slice(point_to_reference_corner_of_cube[2],
                                          point_to_reference_corner_of_cube[2] + max(shape)))] \
        = np.ones([max(shape)]*dimension)
    combinations = [x for x in combinations if np.array_equal(desired_object_from_cube_parts, x)]

    return combinations