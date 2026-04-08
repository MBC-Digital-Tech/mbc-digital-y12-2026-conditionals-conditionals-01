import unittest
import exercises


class TestConditionals(unittest.TestCase):

    def test_check_number(self):
        self.assertEqual(exercises.check_number(5), "positive")
        self.assertEqual(exercises.check_number(-3), "negative")
        self.assertEqual(exercises.check_number(0), "zero")

    def test_even_or_odd(self):
        self.assertEqual(exercises.even_or_odd(4), "even")
        self.assertEqual(exercises.even_or_odd(7), "odd")

    def test_can_vote(self):
        self.assertTrue(exercises.can_vote(18))
        self.assertTrue(exercises.can_vote(45))
        self.assertFalse(exercises.can_vote(17))

    def test_compare_numbers(self):
        self.assertEqual(exercises.compare_numbers(10, 15), "bigger b")
        self.assertEqual(exercises.compare_numbers(20, 5), "bigger a")
        self.assertEqual(exercises.compare_numbers(7, 7), "equal")

    def test_grade_student(self):
        self.assertEqual(exercises.grade_student(95), "Excellence")
        self.assertEqual(exercises.grade_student(75), "Merit")
        self.assertEqual(exercises.grade_student(55), "Achieved")
        self.assertEqual(exercises.grade_student(40), "Not Achieved")

    def test_divisible_by_5_and_3(self):
        self.assertTrue(exercises.divisible_by_5_and_3(15))
        self.assertFalse(exercises.divisible_by_5_and_3(10))
        self.assertFalse(exercises.divisible_by_5_and_3(9))

    def test_triangle_type(self):
        self.assertEqual(exercises.triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(exercises.triangle_type(3, 3, 4), "isosceles")
        self.assertEqual(exercises.triangle_type(3, 4, 5), "scalene")

    def test_is_leap_year(self):
        self.assertTrue(exercises.is_leap_year(2020))
        self.assertFalse(exercises.is_leap_year(2019))

    def test_positive_and_even(self):
        self.assertTrue(exercises.positive_and_even(4))
        self.assertFalse(exercises.positive_and_even(3))
        self.assertFalse(exercises.positive_and_even(-2))

    def test_age_group(self):
        self.assertEqual(exercises.age_group(10), "child")
        self.assertEqual(exercises.age_group(30), "adult")
        self.assertEqual(exercises.age_group(70), "senior")

    def test_multiple_7_or_11(self):
        self.assertEqual(exercises.multiple_7_or_11(14), "divisible by 7")
        self.assertEqual(exercises.multiple_7_or_11(22), "divisible by 11")
        self.assertEqual(exercises.multiple_7_or_11(8), "not divisible")

    def test_famous_building(self):
        self.assertEqual(exercises.famous_building("Wellington"), "The Beehive")
        self.assertEqual(exercises.famous_building("dunedin"), "Larnach Castle")
        self.assertEqual(exercises.famous_building("AUCKLAND"), "Sky Tower")


if __name__ == "__main__":
    unittest.main()
