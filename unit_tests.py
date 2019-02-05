import unittest
from utils import metric2imperial, rand_id


class TestMetricConversion(unittest.TestCase):
    def test_kg2lb(self):
        self.assertEqual(metric2imperial(100, "kg", "lb"), 220.5)

    def test_cm2ft(self):
        self.assertEqual(metric2imperial(100, "cm", "ft"), 3.28)

    def test_invalid(self):
        self.assertEqual(metric2imperial("unknown", "cm", "ft"), "unknown")

    def test_failure(self):
        with self.assertRaises(KeyError):
            metric2imperial(100, "in", "ft")


class TestRandomChar(unittest.TestCase):
    def test_range(self):
        for x in range(100):
            char_id = rand_id()
            self.assertGreaterEqual(char_id, 1)
            self.assertLessEqual(char_id, 87)


if __name__ == '__main__':
    unittest.main()
