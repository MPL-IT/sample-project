import unittest

from sample.hello import greetings


class TestHello(unittest.TestCase):

    def test_basic(self):

        # Arrange
        name = 'Guybrush'

        # Act
        actual = greetings(name)

        # Assert
        expected = 'Hello, Guybrush!'
        self.assertEqual(actual, expected)

