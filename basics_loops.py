mondey_temperatures = [9.1, 8.8, 7.5]

for temperature in mondey_temperatures:
	print(round(temperature))

for letter in "Hello":
	print(letter.title())

student_grades = {"Marry": 9.1, "Sim": 8.8, "john": 7.5}

for students in student_grades.keys():
	print(students)

for grade in student_grades.items():
	print(grade)#return tuples

for gradeonly in student_grades.values():
	print(gradeonly)

a = 3
while a > 0:
	print(a)
	a = a - 1

username = ''
while username != 'pypy':
	username =  input("Enter username 1: ")

while True: #бесконечный цикл
	username = input('Enter username 2: ')
	if username == 'pypy':
		break
	else:
		continue


# print(round(mondey_temperatures[0]))
# print(round(mondey_temperatures[1]))
# print(round(mondey_temperatures[2]))