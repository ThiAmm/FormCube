import unittest


class TestCoordinateSystem(unittest.TestCase):
    def test_coordinateSystemForOnePart(self):
        import numpy as np
        import numpy.testing as nptesting
        from coordinateSystem import getCoordinateSystem

        cube_part = [[[1]]]
        nptesting.assert_equal(getCoordinateSystem([cube_part], [1, 1, 1]), np.array([[[0.]]]))

        cube_part = [[[1, 1]]]
        nptesting.assert_equal(getCoordinateSystem([cube_part], [1, 1, 1]), np.zeros((3, 3, 3)))

if __name__ == '__main__':
    unittest.main()


