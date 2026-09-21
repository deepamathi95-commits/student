import csv
import os


# =========================
# Student Class
# =========================
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_result(self):
        print("\n" + "=" * 45)
        print("           STUDENT RESULT")
        print("=" * 45)
        print(f"Roll Number : {self.roll_no}")
        print(f"Name        : {self.name}")
        print("-" * 45)

        for subject, mark in self.marks.items():
            print(f"{subject:<20}: {mark}")

        print("-" * 45)
        print(f"Total       : {self.calculate_total()}")
        print(f"Average     : {self.calculate_average():.2f}")
        print(f"Grade       : {self.calculate_grade()}")
        print("=" * 45)


# =========================
# Global Student List
# =========================
students = []

SUBJECTS = [
    "Python",
    "Database",
    "Web Development",
    "Communication"
]

CSV_FILE = "student_results.csv"


# =========================
# Add Student
# =========================
def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter Roll Number: ").strip()

    # Check duplicate roll number
    for student in students:
        if student.roll_no == roll_no:
            print("A student with this roll number already exists.")
            return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    marks = {}

    for subject in SUBJECTS:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student = Student(roll_no, name, marks)
    students.append(student)

    print("\nStudent added successfully!")


# =========================
# Display All Students
# =========================
def display_all_students():
    if not students:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 80)
    print("                     ALL STUDENT RESULTS")
    print("=" * 80)

    print(
        f"{'Roll No':<12}"
        f"{'Name':<20}"
        f"{'Total':<10}"
        f"{'Average':<12}"
        f"{'Grade':<10}"
    )

    print("-" * 80)

    for student in students:
        print(
            f"{student.roll_no:<12}"
            f"{student.name:<20}"
            f"{student.calculate_total():<10.2f}"
            f"{student.calculate_average():<12.2f}"
            f"{student.calculate_grade():<10}"
        )

    print("=" * 80)


# =========================
# Search Student
# =========================
def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:
        if student.roll_no == roll_no:
            student.display_result()
            return

    print("Student not found.")


# =========================
# Update Student Marks
# =========================
def update_student():
    print("\n--- Update Student ---")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:

        if student.roll_no == roll_no:

            print(f"\nStudent Name: {student.name}")

            for subject in SUBJECTS:
                while True:
                    try:
                        mark = float(
                            input(
                                f"Enter new marks for {subject} "
                                f"(current: {student.marks[subject]}): "
                            )
                        )

                        if 0 <= mark <= 100:
                            student.marks[subject] = mark
                            break
                        else:
                            print("Marks must be between 0 and 100.")

                    except ValueError:
                        print("Please enter a valid number.")

            print("\nStudent result updated successfully!")
            return

    print("Student not found.")


# =========================
# Delete Student
# =========================
def delete_student():
    print("\n--- Delete Student ---")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:

        if student.roll_no == roll_no:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


# =========================
# Save Students to CSV
# =========================
def save_to_csv():
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Roll No",
                "Name",
                "Python",
                "Database",
                "Web Development",
                "Communication",
                "Total",
                "Average",
                "Grade"
            ])

            for student in students:
                writer.writerow([
                    student.roll_no,
                    student.name,
                    student.marks["Python"],
                    student.marks["Database"],
                    student.marks["Web Development"],
                    student.marks["Communication"],
                    student.calculate_total(),
                    f"{student.calculate_average():.2f}",
                    student.calculate_grade()
                ])

        print(f"\nStudent records saved to '{CSV_FILE}'.")

    except Exception as e:
        print("Error while saving file:", e)


# =========================
# Load Students from CSV
# =========================
def load_from_csv():
    if not os.path.exists(CSV_FILE):
        print("\nNo existing CSV file found.")
        return

    students.clear()

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                marks = {
                    "Python": float(row["Python"]),
                    "Database": float(row["Database"]),
                    "Web Development": float(row["Web Development"]),
                    "Communication": float(row["Communication"])
                }

                student = Student(
                    row["Roll No"],
                    row["Name"],
                    marks
                )

                students.append(student)

        print(f"\nLoaded {len(students)} student record(s).")

    except Exception as e:
        print("Error while loading file:", e)


# =========================
# Main Menu
# =========================
def main():
    load_from_csv()

    while True:

        print("\n")
        print("=" * 45)
        print("      STUDENT RESULT MANAGEMENT")
        print("=" * 45)
        print("1. Add Student")
        print("2. Display All Results")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Results to CSV")
        print("7. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_all_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            save_to_csv()

        elif choice == "7":
            save_to_csv()
            print("\nThank you for using Student Result Management System!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


# =========================
# Program Start
# =========================
if __name__ == "__main__":
    main()