print("*****Student Result System*****")
n=input("enter the number of students") 
total_percentage=0
highest=0
topper_name=""
fail_count=0
for i in range(n):
    print("\nStudent",i+1)
    name =input("enter student name:")
    m1=int(input("enter marks of subject 1:"))
    m2 =int(input("enter marks of subject 2:"))
    m3=int(input("enter marks of subject 3:"))
    total=m1+m2+m3
    percentage=total/3
    total_percentage +=percentage
    if m1<33 or m2<33 or m3<33:
        grade="fail"
        fail_count+=1
        
    else:
        if percentage>=90:
           grade="A+"
        elif percentage>=75:
           grade="A"
        elif percentage>=60:
           grade="B"
        elif percentage>=40:
           grade="C"
        else:
         grade="fail"
         fail_count+=1
    if percentage>highest:
        highest=percentage
        topper_name=name
    print("name:",name)
    print("percentage:",percentage)
    print("grade",grade)
avg=total_percentage/5
print("\nClass Average Percentage:",avg)
print("Topper Name:",topper_name)
print("Highest percentage:",highest)
print("total failed students:",fail_count)
