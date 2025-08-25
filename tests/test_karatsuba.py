import random
import unittest
from main import karatsuba

class TestKaratsuba(unittest.TestCase):
    def test_small_numbers(self):
        for a in range(-20, 21):
            for b in range(-20, 21):
                self.assertEqual(karatsuba(a, b), a*b)

    def test_medium_random(self):
        rng = random.Random(0)
        for _ in range(100):
            a = rng.randint(-10**40, 10**40)
            b = rng.randint(-10**40, 10**40)
            self.assertEqual(karatsuba(a, b), a*b)

    def test_large(self):
        a = int("314159265358979323846264338327950288419716939937510")
        b = int("271828182845904523536028747135266249775724709369995")
        self.assertEqual(karatsuba(a, b), a*b)

if __name__ == "__main__":
    unittest.main()

