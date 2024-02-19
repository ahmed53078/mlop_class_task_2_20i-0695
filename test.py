import unittest
from main import StudentsInMLOps

class TestStudentsInMLOps(unittest.TestCase):
    def setUp(self):
        self.mlops_class = StudentsInMLOps()

    def test_enroll_students(self):
        self.mlops_class.enrollStudents(10)
        self.assertEqual(self.mlops_class.getTotalStrength(), 10)

    def test_drop_students(self):
        self.mlops_class.enrollStudents(10)
        self.mlops_class.dropStudents(5)
        self.assertEqual(self.mlops_class.getTotalStrength(), 5)

    def test_get_total_strength(self):
        self.mlops_class.enrollStudents(10)
        self.assertEqual(self.mlops_class.getTotalStrength(), 10)

    def test_get_class_name(self):
        self.assertEqual(self.mlops_class.getClassName(), "MLOps")

if _name_ == '_main_':
    unittest.main()
