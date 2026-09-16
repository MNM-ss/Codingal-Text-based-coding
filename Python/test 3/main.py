students = {
	"Manha": 88,
	"Nusayba": 100,
	"Tashriq": 76,
	"Faizaan": 84,
	"Rudrangsho": 91
}

total_score = 0
for score in students.values():
	total_score += score

average = total_score / len(students)
print("Class average:", average)

highest_score = max(students.values())
lowest_score = min(students.values())

top_student = max(students, key=students.get)
bottom_student = min(students, key=students.get)

print("Top scorer:", top_student, "with", highest_score)
print("Bottom scorer:", bottom_student, "with", lowest_score)

student_name = input("Enter a student name: ")
student_score = students.get(student_name)

if student_score is not None:
	print(student_name, "scored", student_score)
else:
	print("Student not found.")
	
