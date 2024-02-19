class StudentsInMLOps:
    def _init_(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, num_students):
        if num_students > 0:
            self.total_strength += num_students
            print(f"{num_students} students enrolled in {self.class_name}.")

    def dropStudents(self, num_students):
        if num_students > 0:
            self.total_strength -= num_students
            print(f"{num_students} students dropped from {self.class_name}.")

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name

# Example usage:
if _name_ == "_main_":
    mlops_class = StudentsInMLOps()
    print("Class name:", mlops_class.getClassName())
    mlops_class.enrollStudents(10)
    mlops_class.enrollStudents(5)
    mlops_class.dropStudents(2)
    print("Total strength:", mlops_class.getTotalStrength())
