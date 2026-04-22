import unittest
from age import categorize_by_age

class TestSubtestAge(unittest.TestCase):

    def test_1_child_range(self):
        print()
        for age in range(0, 10):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")
                print(f"{age} is considered as a Child.")

    def test_2_adolescent_range(self):
        print()
        for age in range(10, 19):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adolescent")
                print(f"{age} is considered as a Adolescent.")

    def test_3_adult_range(self):
        print()
        for age in range(19, 66):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")
                print(f"{age} is considered as a Adult.")

if __name__ == "__main__":
    unittest.main(verbosity=2)