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
