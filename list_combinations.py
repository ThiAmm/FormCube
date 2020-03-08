def list_combinations(cube_parts, shape, dimension=3):
    from list_rotations import list_rotations
    from coordinateSystem import getCoordinateSystem
    from coordinateSystem import getPointToReferenceCornerOfCube
    from coordinateSystem import getObjectInCoordinateSystem
    import numpy as np
    import itertools

    coordinateSystem = getCoordinateSystem(cube_parts, shape, dimension)
    point_to_reference_corner_of_cube = getPointToReferenceCornerOfCube(cube_parts, dimension)

    combinations = [coordinateSystem]
    for cube_part in cube_parts:
        combinations_new = []
        for combination in combinations:
            for index in itertools.product(*[range(0, n) for n in shape]):
                position_in_cube = np.add(point_to_reference_corner_of_cube, np.array(index))
                cube_part_in_reference_array = np.zeros(coordinateSystem.shape)
                cube_part_in_reference_array[(slice(position_in_cube[0], position_in_cube[0] + cube_part.shape[0]),
                                              slice(position_in_cube[1], position_in_cube[1] + cube_part.shape[1]),
                                              slice(position_in_cube[2], position_in_cube[2] + cube_part.shape[2]))] \
                    += cube_part
                for rotated_cube_part in list_rotations(cube_part_in_reference_array, dimension):
                    combination_with_rotated_cube_part = combination + rotated_cube_part
                    combinations_new.append(combination_with_rotated_cube_part)
        combinations = combinations_new

    desired_object_from_cube_parts = getObjectInCoordinateSystem(coordinateSystem, point_to_reference_corner_of_cube,
                                                                 shape, dimension)

    combinations = [x for x in combinations if np.array_equal(desired_object_from_cube_parts, x)]

    return combinations
