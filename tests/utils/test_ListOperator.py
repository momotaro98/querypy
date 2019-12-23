import unittest
from querypy.utils import ListOperator


class TestListOperator(unittest.TestCase):
    def test_progressive_comparison_True(self):
        # Arrange
        vector = [1, 2, 3]
        bf = lambda x, y: x < y
        # Act
        result = ListOperator.progressive_comparison(vector, bf)
        # Assert
        self.assertTrue(result)

    def test_progressive_comparison_False(self):
        # Arrange
        vector = [1, 3, 2]
        bf = lambda x, y: x < y
        # Act
        result = ListOperator.progressive_comparison(vector, bf)
        # Assert
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
