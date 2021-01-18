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

    def test_bad_pirat_raises_exception(self):

        # Arrange
        name = 'LeChuck'

        # Act / Assert
        with self.assertRaises(ValueError):
            greetings(name)
