import random
import time

students = ["Harry", "Marge", "Billy", "Lottie"]
students.append("Sam")
students.insert(2, "Mike")

print("These are the students still in the class: ")
for student in students:
  time.sleep(0.5)
  print(student)
  
time.sleep(1)

choice = random.randint(0,len(students)-1)
student_to_remove = students[choice]
print("You are about to remove: " + student_to_remove + " from the class...")
time.sleep(1)
del students[choice]

print("These are the students still in the class, in reverse order")
for i in range(len(students)-1,-1,-1):
  time.sleep(0.5)
  print(students[i])
