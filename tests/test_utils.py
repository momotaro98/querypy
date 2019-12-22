import unittest
from querypy.utils import ListOperator


class TestUtils(unittest.TestCase):
    def test_progressive_comparison_True(self):
        # Arrange
        vector = [1, 2, 3]
        bf = lambda x, y: x < y
        # Act
        actual = ListOperator.progressive_comparison(vector, bf)
        # Assert
        self.assertTrue(actual)

    def test_progressive_comparison_False(self):
        # Arrange
        vector = [1, 3, 2]
        bf = lambda x, y: x < y
        # Act
        actual = ListOperator.progressive_comparison(vector, bf)
        # Assert
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
