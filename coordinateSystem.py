def getCoordinateSystem(cube_parts, shape, dimension=3):
    import numpy as np

    maximalLengthOfCubePart = getMaximalLengthOfCubePart(cube_parts)
    length_of_coordinateSystem_in_all_dimensions = max(shape) + (maximalLengthOfCubePart - 1) * 2
    return np.zeros([length_of_coordinateSystem_in_all_dimensions] * dimension)


def getPointToReferenceCornerOfCube(cube_parts, shape, dimension):
    from operator import add

    coordinateSystem = getCoordinateSystem(cube_parts, shape, dimension)
    maximal_length_of_cube_part = getMaximalLengthOfCubePart(cube_parts)
    coordinateSystem_Edge = tuple(-1*x for x in coordinateSystem.shape)
    return list(map(add, coordinateSystem_Edge, [maximal_length_of_cube_part] * dimension))


def getMaximalLengthOfCubePart(cube_parts):
    import numpy as np
    shapes_of_cube_parts = map(np.shape, cube_parts)
    return max(max(shape_of_cube_part) for shape_of_cube_part in shapes_of_cube_parts)

def getObjectInCoordinateSystem(coordinateSystem,point_to_reference_corner_of_cube,shape,dimension=3):
    import numpy as np
    desired_object_from_cube_parts = np.zeros(coordinateSystem.shape)
    desired_object_from_cube_parts[(slice(point_to_reference_corner_of_cube[0],
                                          point_to_reference_corner_of_cube[0]+max(shape)
                                          ),
                                    slice(point_to_reference_corner_of_cube[1],
                                          point_to_reference_corner_of_cube[1] + max(shape)
                                          ),
                                    slice(point_to_reference_corner_of_cube[2],
                                          point_to_reference_corner_of_cube[2] + max(shape)))] \
        = np.ones([max(shape)]*dimension)
    return desired_object_from_cube_parts
