""" Implement a function called sort_students that takes a list of student
object as input and sorts the list based on their CGPA in descending order
Each student object has the following attributes name(string),
roll_number(string),and cgpa(float).Test the function with different input list of the students. """


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of the Students in the descending order of the cgpa
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  #syntax lambda arg:exp
  return sorted_students


#Example usage
students = [
    Student("Christina", "A123", 9.5),
    Student("Ramya", "A124", 9.6),
    Student("Jeeva", "A125", 8.3),
    Student("Vetri", "A126", 8.7)
]

sorted_students = sort_students(students)

#Print the sorted list of students
for student in sorted_students:
  print("Name:{},Roll Number:{},CGPA:{}".format(student.name,
                                                student.roll_number,
                                                student.cgpa))
