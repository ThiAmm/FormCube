import unittest

import numpy as np
import numpy.testing as nptesting

from combinations import get_combinations


class TestCoordinateSystem(unittest.TestCase):

    def test_combinationForSimpleObject(self):
        cube_part = np.array([[[1]]])
        coordinate_system = np.array([[[0.]]])
        combinations = get_combinations(coordinate_system,
                                        point_to_reference_corner_of_cube=[0, 0, 0],
                                        cube_parts=[cube_part],
                                        shape=(1, 1, 1),
                                        dimension=3)
        nptesting.assert_equal(len(combinations), 24)

    def test_combinationForTwoSimpleObjects(self):
        cube_parts = [np.array([[[1]]]), np.array([[[1]]])]
        coordinate_system = np.array([[[0.], [0.]]])
        combinations = get_combinations(coordinate_system,
                                        point_to_reference_corner_of_cube=[0, 0, 0],
                                        cube_parts=cube_parts,
                                        shape=(1, 2, 1),
                                        dimension=3)
        nptesting.assert_equal(len(combinations), 24 * 24 * 4)

    if __name__ == '__main__':
        unittest.main()
