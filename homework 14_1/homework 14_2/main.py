from student import Student
from group import Group, GroupFullException

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

    assert gr.find_student('Jobs') == st1, 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'

    gr.delete_student('Taylor')
    print(gr)  # Only one student

    gr.delete_student('Taylor')  # No error!