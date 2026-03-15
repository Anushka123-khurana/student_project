print("student result management system")
name =input("enter student name")
sub1=int(input("enter marks of subject1"))
sub2=int(input("enter marks of subject2"))
sub3=int(input("enter marks of subject3"))
total=sub1+sub2+sub3
percentage=total/3
print("\n---RESULT---")
print("Student name:",name)
print("total marks:",total)
print("percentage:",percentage)
if percentage >=90:
    grade ="A+"
elif percentage >=75:
    grade ="A"
elif percentage >=60:
    grade ="B"
else:
    grade ="fail"
print("grade:",grade)
