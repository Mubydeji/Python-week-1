# -----------------------------
# Student grading & statistics
# -----------------------------

students = [
    {"name": "Amina", "assignment": 78, "test": 82, "exam": 90},
    {"name": "Yusuf", "assignment": 65, "test": 70, "exam": 68},
    {"name": "Zainab", "assignment": 88, "test": 91, "exam": 94},
    {"name": "Musa", "assignment": 45, "test": 50, "exam": 48},
    {"name": "Sadiq", "assignment": 72, "test": 75, "exam": 80}
]


def weighted_total(student):
    return (
        0.30 * student["assignment"] +
        0.30 * student["test"] +
        0.40 * student["exam"]
    )


def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


# ---- Compute totals & grades ----
totals = []
grade_distribution = {}

for student in students:
    total = weighted_total(student)
    grade = letter_grade(total)

    student["total"] = round(total, 2)
    student["grade"] = grade

    totals.append(total)
    grade_distribution[grade] = grade_distribution.get(grade, 0) + 1


# ---- Class statistics ----
def mean(values):
    return sum(values) / len(values)


def median(values):
    values = sorted(values)
    n = len(values)
    mid = n // 2

    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]


class_mean = round(mean(totals), 2)
class_median = round(median(totals), 2)


# ---- Text report ----
report = []
report.append("CLASS PERFORMANCE REPORT")
report.append("-" * 25)
report.append(f"Number of students: {len(students)}")
report.append(f"Class mean score: {class_mean}")
report.append(f"Class median score: {class_median}")
report.append("\nGrade Distribution:")

for grade in sorted(grade_distribution.keys()):
    report.append(f"{grade}: {grade_distribution[grade]}")

report.append("\nIndividual Results:")
for s in students:
    report.append(
        f"{s['name']}: Total = {s['total']}, Grade = {s['grade']}"
    )


# ---- Output report ----
print("\n".join(report))
