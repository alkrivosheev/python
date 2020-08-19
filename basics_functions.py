def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    elif type(value) == list:
        the_mean = sum(value) / len(value)
    else:
        the_mean  = None
    return the_mean

print(mean([1, 5, 6, 8]))
student_grades = {"Marry": 9.1, "Sim": 8.8, "john": 7.5}
print(mean(student_grades))
print(mean(1))#test
print("hello test")
