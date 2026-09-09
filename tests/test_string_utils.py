import unittest

from string_utils import reverse_words


class StringTests(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("hello cloud agent"), "agent cloud hello")

    def test_whitespace(self):
        self.assertEqual(reverse_words("  hello   world "), "world hello")


if __name__ == "__main__":
    unittest.main()
