import unittest

from lfhohmann.helloworld import say_hello


class SayHello(unittest.TestCase):
    def test_no_name(self):
        self.assertEqual(say_hello(), "Hello, world!")

    def test_valid_name(self):
        self.assertEqual(say_hello("Lucas"), "Hello, Lucas!")
        self.assertEqual(say_hello("Lucas Hohmann"), "Hello, Lucas Hohmann!")
