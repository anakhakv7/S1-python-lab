student={"Name":"Anqa","Roll.NO":8,"Register number":"MCA007","Department":"CS","Semester":2}
print(student)
total_mark=int(input("Enter the total mark of the student: "))
student.update({"total_mark": total_mark})
mark=student["total_mark"]
if mark >=90:
    grade="A"
elif mark >=82:
    grade="B"
elif mark >=75:
    grade="C"
elif mark >=60:
    grade="D"
elif mark >=50:
    grade="P"
else:
    grade="F"
student.update({"grade":grade})
print(student)
del student["Roll.NO"]
print(student)


