
import matplotlib.pyplot as plt
import pandas as pd

students = [
    {
        "name": "Ali",
        "marks": {"Python": 85, "SQL": 78, "Statistics": 90},
        "present": 45,
        "total_classes": 50
    },
    {
        "name": "Sara",
        "marks": {"Python": 92, "SQL": 88, "Statistics": 95},
        "present": 48,
        "total_classes": 50
    },
    {
        "name": "Ahmed",
        "marks": {"Python": 45, "SQL": 52, "Statistics": 48},
        "present": 35,
        "total_classes": 50
    },
    {
        "name": "Ayesha",
        "marks": {"Python": 75, "SQL": 82, "Statistics": 79},
        "present": 46,
        "total_classes": 50
    }
]


# 1. Calculate average marks
def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks.values()) / len(marks)


# 2. Assign grade
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "A-"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "B-"
    elif average >= 50:
        return "C"
    else:
        return "D"


# 3. Check pass or fail
def check_pass_status(marks, pass_marks=50):
    return all(
        mark >= pass_marks for mark in marks.values()
    )


# 4. Calculate class average
def calculate_class_average(students):
    if not students:
        return 0

    averages = [
        calculate_average(student["marks"])
        for student in students
    ]
    return sum(averages) / len(averages)


# 5. Find top student
def find_top_student(students):
    if not students:
        return None

    return max(
        students,
        key=lambda student: calculate_average(student["marks"])
    )


# 6. Calculate subject averages
def subject_average(students):
    if not students:
        return {}

    subjects = students[0]["marks"].keys()

    return {
        subject: sum(
            student["marks"][subject]
            for student in students
        ) / len(students)
        for subject in subjects
    }


# 7. Rank students
def rank_students(students):
    return sorted(
        students,
        key=lambda student: calculate_average(student["marks"]),
        reverse=True
    )


# 8. Calculate attendance percentage
def attendance_percentage(student):
    total = student["total_classes"]

    if total <= 0:
        return 0

    return student["present"] / total * 100


# 9. Identify students at risk
def identify_student_at_risk(students, threshold=50):
    return [
        student["name"]
        for student in students
        if calculate_average(student["marks"]) < threshold
    ]


# 10. Plot subject averages
def plot_average_subject(students):
    averages = subject_average(students)

    if not averages:
        print("No student data available to plot.")
        return

    plt.bar(
        averages.keys(),
        averages.values()
    )
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()


# Main program
if __name__ == "__main__":

    print("Class Average:",
          round(calculate_class_average(students), 2))

    top = find_top_student(students)
    if top:
        print("Top Student:", top["name"])

    print("\n===============================")
    print("|       STUDENT REPORT        |")
    print("===============================")

    report = []

    for student in students:
        average = calculate_average(student["marks"])

        report.append({
            "Name": student["name"],
            "Average": round(average, 2),
            "Grade": assign_grade(average),
            "Status": (
                "Pass" if check_pass_status(student["marks"])
                else "Fail"
            ),
            "Attendance (%)": round(
                attendance_percentage(student), 2
            )
        })

    df = pd.DataFrame(report)
    print(df.to_string(index=False))

    print("\nSUBJECT AVERAGES:")
    for subject, average in subject_average(students).items():
        print(f"{subject}: {average:.2f}")

    print("\nSTUDENT RANKING:")
    for rank, student in enumerate(rank_students(students), start=1):
        print(
            rank,
            student["name"],
            round(calculate_average(student["marks"]), 2)
        )

    print("\nSTUDENTS NEEDING SUPPORT:")
    at_risk = identify_student_at_risk(students)
    print(at_risk if at_risk else "No students identified.")

    plot_average_subject(students)
