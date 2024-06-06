class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"Gender: {self.gender}, Age: {self.age}, Name: {self.first_name} {self.last_name}"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"Student: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}, Record Book: {self.record_book}"


class GroupFullException(Exception):
    pass


class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise GroupFullException("Group is full. Cannot add more than 10 students.")
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\n{all_students}"


if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
    st4 = Student('Female', 24, 'Jane', 'Doe', 'AN147')
    st5 = Student('Male', 21, 'Mike', 'Brown', 'AN148')
    st6 = Student('Female', 23, 'Anna', 'Smith', 'AN149')
    st7 = Student('Male', 20, 'Tom', 'White', 'AN150')
    st8 = Student('Female', 22, 'Lucy', 'Black', 'AN151')
    st9 = Student('Male', 23, 'Jack', 'Green', 'AN152')
    st10 = Student('Female', 21, 'Sue', 'Blue', 'AN153')
    st11 = Student('Male', 22, 'Mark', 'Yellow', 'AN154')

    gr = Group('PD1')
    try:
        gr.add_student(st1)
        gr.add_student(st2)
        gr.add_student(st3)
        gr.add_student(st4)
        gr.add_student(st5)
        gr.add_student(st6)
        gr.add_student(st7)
        gr.add_student(st8)
        gr.add_student(st9)
        gr.add_student(st10)
        gr.add_student(st11)  # This should raise GroupFullException
    except GroupFullException as e:
        print(e)

    print(gr)

    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

    gr.delete_student('Taylor')
    print(gr)  # Only one student

    gr.delete_student('Taylor')  # No error!