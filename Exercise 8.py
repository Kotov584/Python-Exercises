student_names = []
student_course_a_grades = []
student_course_b_grades = []
student_name = input("Write your name:\r\n")
student_course_a_grade = int(input("Write your grade in course A: \r\n"))
student_course_b_grade = int(input("Write your grade in course B: \r\n"))
student_names.append(student_name)
student_course_a_grades.append(student_course_a_grade)
student_course_b_grades.append(student_course_b_grade)
current_key = int(0)
for i in student_names:
    print("----\r\nStudent:\r\nCourse A grade:",student_course_a_grades[current_key], "Course B grade:",student_course_b_grades[current_key])
    student_course_average_grade = student_course_a_grades[current_key]+student_course_b_grades[current_key]
    student_course_average_grade = student_course_average_grade/2
    print("Average grade: ", student_course_average_grade)
    current_key = current_key + 1 
print("----")
print("The lowest grade for course A: ", min(student_course_a_grades))
to_devide = int(0)
for i in student_course_a_grades:
  to_devide = to_devide + 1
  
total_grade_all = 0
print("The average grade of all students: ",total_grade_all)