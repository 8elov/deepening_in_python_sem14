import unittest
from triangle import Triangle, InvalidTriangleError


class TestTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        """We check that the right triangle does not throw an exception."""
        self.assertIsNotNone(Triangle(3, 4, 5))

    def test_invalid_triangle(self):
        """Verify that an invalid triangle raises an InvalidTriangleError."""
        with self.assertRaises(InvalidTriangleError):
            Triangle(1, 1, 2)

    def test_classify_triangle(self):
        """Check that the classify_triangle method correctly
        classifies triangles."""
        triangle = Triangle(3, 3, 3)
        self.assertEqual(triangle.classify_triangle(),
                         'Равносторонний треугольник')

        triangle = Triangle(3, 4, 4)
        self.assertEqual(triangle.classify_triangle(),
                         'Равнобедренный треугольник')

        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.classify_triangle(),
                         'Разносторонний треугольник')


if __name__ == '__main__':
    unittest.main(verbosity=10)
