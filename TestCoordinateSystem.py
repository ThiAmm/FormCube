import unittest

from coordinateSystem import getPointToReferenceCornerOfCube
import numpy as np
import numpy.testing as nptesting


class TestCoordinateSystem(unittest.TestCase):
    def test_coordinateSystemForOnePart(self):
        from coordinateSystem import getCoordinateSystem

        cube_part = [[[1]]]
        nptesting.assert_equal(getCoordinateSystem([cube_part], [1, 1, 1]), np.array([[[0.]]]))

        cube_part = [[[1, 1]]]
        nptesting.assert_equal(getCoordinateSystem([cube_part], [1, 1, 1]), np.zeros((3, 3, 3)))

    def test_ReferenceCornerOfDesiredObject(self):
        cube_part = [[1]]
        self.assertEqual(getPointToReferenceCornerOfCube([cube_part], (1, 1, 1), 3), [0, 0, 0])
        cube_part = [[1, 1]]
        self.assertEqual(getPointToReferenceCornerOfCube([cube_part], (1, 1, 1), 3), [-1, -1, -1])


if __name__ == '__main__':
    unittest.main()
