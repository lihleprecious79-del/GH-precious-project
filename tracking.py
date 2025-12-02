

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  

    def add_grade(self, assignment, score):
        self.grades.append((assignment, score))

    def average(self):
        if not self.grades:
            return 0
        return sum(score for _, score in self.grades) / len(self.grades)

    def __str__(self):
        grade_list = "\n".join([f"   - {a}: {s}" for a, s in self.grades])
        return f"Student: {self.name}\nGrades:\n{grade_list}\nAverage: {self.average():.2f}\n"


class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print("Student already exists.")
        else:
            self.students[name] = Student(name)
            print(f"Added {name}")

    def add_grade(self, name, assignment, score):
        if name not in self.students:
            print("Student not found.")
        else:
            self.students[name].add_grade(assignment, score)
            print(f"Added grade to {name}")

    def show_student(self, name):
        if name not in self.students:
            print("Student not found.")
        else:
            print(self.students[name])

    def show_all(self):
        if not self.students:
            print("No students recorded.")
        for student in self.students.values():
            print(student)

def main():
    tracker = GradeTracker()

    while True:
        print("\n--- Grade Tracker Menu ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Add student marks")
        print("4. Show Student Report")
        print("5. Show All Students")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            tracker.add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            assignment = input("Assignment name: ")
            try:
                score = float(input("Score (0–100): "))
                tracker.add_grade(name, assignment, score)
            except ValueError:
                print("Invalid score.")

        elif choice == "3":
            name = input("Enter student name: ")
            tracker.show_student(name)

        elif choice == "4":
            tracker.show_all()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
