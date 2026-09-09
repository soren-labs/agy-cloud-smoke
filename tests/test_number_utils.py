import unittest

from number_utils import clamp


class ClampTests(unittest.TestCase):
    def test_inside(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_lower(self):
        self.assertEqual(clamp(-1, 0, 10), 0)

    def test_upper(self):
        self.assertEqual(clamp(11, 0, 10), 10)

    def test_invalid_interval(self):
        with self.assertRaises(ValueError):
            clamp(1, 10, 0)


if __name__ == "__main__":
    unittest.main()
