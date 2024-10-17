class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name            # Instanzvariable, eindeutig für jede Instanz
        Student.student_count += 1  # Zugriff auf die Klassenvariable über den Klassennamen

    @classmethod
    def get_student_count(cls):
        # Klassenmethode, die den Wert der Klassenvariable zurückgibt
        return cls.student_count



print("Zugriffe über die Klasse auf die Klassenfunktion")
print(Student.get_student_count())  # 0

student1 = Student("Alice")
student2 = Student("Bob")

print(Student.get_student_count())  # 2


print("Zugriffe über die Objekte auf die Klassenfunktion")
print(student1.student_count)       # 2
print(student2.student_count)       # 2
