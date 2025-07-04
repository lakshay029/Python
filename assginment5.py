#task1
Student_marks={'Alice':'83','Sam':'74','lio':'44'}
student_name=input("enter the name: ")

if student_name in Student_marks:
    print(f"{student_name}'s marks: {Student_marks[student_name]}")
else:
    print(f"Record of this{student_name} not found")

#task2
numbers=list(range(1,11))
first_five=numbers[:5]
reverse_five=numbers[:5]

print("original list is: ",numbers)
print("first five numbers are: ",first_five)
print("last five numbers are: ",reverse_five)