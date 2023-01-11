class Student:
    student_id=4
    student_name="raju"
Student.student_clss='10'
for i,j in Student.__dict__.items():
    print(i,j)
print("after delete")
del Student.student_name
for i,j in Student.__dict__.items():
    print(i,j)