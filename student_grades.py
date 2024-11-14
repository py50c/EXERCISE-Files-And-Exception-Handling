# student_grades.py

# Step 1: Open students.txt and read the contents
with open('students.txt', 'r') as file:
    students = file.readlines()

# Step 2: Print each line in the file
print("Contents of students.txt:")
for line in students:
    print(line.strip())

# Step 3: Calculate the average grade
grades = [int(line.split(", ")[1]) for line in students]
average_grade = sum(grades) / len(grades)
print(f"\nAverage Grade: {average_grade:.2f}")

# Step 4: Find students who scored above the average
above_average_students = [line.split(", ")[0] for line in students if int(line.split(", ")[1]) > average_grade]

# Step 5: Write results to results.txt
with open('results.txt', 'w') as file:
    file.write(f"Average Grade: {average_grade:.2f}\n")
    file.write("Students scoring above average:\n")
    for student in above_average_students:
        file.write(f"- {student}\n")

print("\nResults written to results.txt")
