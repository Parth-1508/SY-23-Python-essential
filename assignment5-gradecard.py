# Average Grade Calculator

num_students = int(input("Enter the number of students: "))

class_total = 0

for i in range(1, num_students + 1):
    print(f"\nEnter marks for Student {i}:")
    student_total = 0

    for j in range(1, 6):
        mark = float(input(f"Test {j}: "))
        student_total += mark

    student_average = student_total / 5
    print(f"Average of Student {i}: {student_average:.2f}")

    class_total += student_total

overall_average = class_total / (num_students * 5)

print("\nOverall Class Average:", round(overall_average, 2))