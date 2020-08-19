mondey_temperatures = [9.1, 8.8, 7.5]#Список list можно добавлять элементы
mondey_temperatures.append(7.8)
mondey_temperatures.clear()
student_grades = {"Marry": 9.1, "Sim": 8.8, "john": 7.5}#Словарь
sunday_temperatures = (1, 5, 6)#кортеж нельзя добавлять элементы tuple


mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)
print(sunday_temperatures)
print(mondey_temperatures)