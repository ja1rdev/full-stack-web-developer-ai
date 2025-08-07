# Define list of tuples
student_list = [
    ("Fazt", 5.0),
    ("Web", 4.0),
    ("Tech", 3.0)
]

# Inicialize with 0 
max_note = 0
name = ""

# Scroll list
for name, note in student_list:
    if note > max_note:
        max_note = note
        best_student = name

print(f"The student with the highest grade is {best_student} ({max_note}).")