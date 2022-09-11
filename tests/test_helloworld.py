"""Unit Tests for 'helloworld' module"""

import unittest

from lfhohmann.helloworld import say_bye, say_hello


class SayHello(unittest.TestCase):
    """Test case for 'say_hello()' function"""

    def test_no_name(self):
        """Test function without a <name> argument"""

        self.assertEqual(say_hello(), "Hello, world!")

    def test_valid_name(self):
        """Test function with <name> argument"""

        self.assertEqual(say_hello("Lucas"), "Hello, Lucas!")
        self.assertEqual(say_hello("Lucas Hohmann"), "Hello, Lucas Hohmann!")


class SayBye(unittest.TestCase):
    """Test case for 'say_bye()' function"""

    def test_no_name(self):
        """Test function without a <name> argument"""

        self.assertEqual(say_bye(), "Bye, world!")

    def test_valid_name(self):
        """Test function with <name> argument"""

        self.assertEqual(say_bye("Lucas"), "Bye, Lucas!")
        self.assertEqual(say_bye("Lucas Hohmann"), "Bye, Lucas Hohmann!")
