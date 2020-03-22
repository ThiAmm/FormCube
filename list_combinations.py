def list_combinations(cube_parts, shape, dimension=3):
    from coordinateSystem import getCoordinateSystem
    from coordinateSystem import getPointToReferenceCornerOfCube
    from coordinateSystem import getObjectInCoordinateSystem
    from combinations import get_combinations
    import numpy as np
    import itertools

    coordinateSystem = getCoordinateSystem(cube_parts, shape, dimension)
    point_to_reference_corner_of_cube = getPointToReferenceCornerOfCube(cube_parts, dimension)

    combinations = get_combinations(coordinateSystem, point_to_reference_corner_of_cube, cube_parts, shape, dimension)

    desired_object_from_cube_parts = getObjectInCoordinateSystem(coordinateSystem, point_to_reference_corner_of_cube,
                                                                 shape, dimension)

    combinations = [x for x in combinations if np.array_equal(desired_object_from_cube_parts, x)]

    return combinations
