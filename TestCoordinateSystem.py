import unittest

from coordinateSystem import getPointToReferenceCornerOfCube
from coordinateSystem import getCoordinateSystem
from coordinateSystem import getObjectInCoordinateSystem
import numpy as np
import numpy.testing as nptesting


class TestCoordinateSystem(unittest.TestCase):
    def test_coordinateSystemForOnePart(self):
        cube_part = np.array([[[1]]])
        nptesting.assert_equal(getCoordinateSystem([cube_part], [1, 1, 1]), np.array([[[0.]]]))

        cube_part = [[[1, 1]]]
        nptesting.assert_equal(getCoordinateSystem([cube_part], [1, 1, 1]), np.zeros((3, 3, 3)))

    def test_ReferenceCornerOfDesiredObject(self):
        cube_part = np.array([[1]])
        self.assertEqual(getPointToReferenceCornerOfCube([cube_part], (1, 1, 1), 3), [0, 0, 0])
        cube_part = np.array([[1, 1]])
        self.assertEqual(getPointToReferenceCornerOfCube([cube_part], (1, 1, 1), 3), [-1, -1, -1])

    def test_Object_For_SimpleShapes(self):
        coordinateSystem = np.array([[[0.]]])
        nptesting.assert_equal(getObjectInCoordinateSystem(coordinateSystem, [0, 0, 0], (1, 1, 1)),
                               np.array([[[1]]]))

    def test_ObjectWith_LengthTwoTimesOneIsGeneratedCorrectlyInTheCoordinateSystem(self):
        coordinateSystem = np.array([[[0.,0.,0.],[0.,0.,0.]]])
        nptesting.assert_equal(getObjectInCoordinateSystem(coordinateSystem, [0, 0, 0], (1, 2, 1)),
                               np.array([[[1.,0.,0.],[1.,0.,0.]]]))

    def test_ObjectWith_LengthOneTimesTwoIsGeneratedCorrectlyInTheCoordinateSystem(self):
        coordinateSystem = np.array([[[0., 0., 0.]], [[0., 0., 0.]]])
        nptesting.assert_equal(getObjectInCoordinateSystem(coordinateSystem, [0, 0, 0], (2, 1, 1)),
                               np.array([[[1., 0., 0.]], [[1., 0., 0.]]]))

if __name__ == '__main__':
    unittest.main()