# Average Height Exercise

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total_height = 0
for height in student_heights:
   total_height = total_height + height
print(total_height)

number_of_students = 0
for student in student_heights:
   number_of_students += 1

average_height = round(total_height / number_of_students)
print(average_height)

##############################################################
# Exercise 5-2 Highest Score 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇 
highest_score = 0 

for num in student_scores:
   if(highest_score is 0 or num > highest_score):
      highest_score = num

print(f"The highest score in the class is: {highest_score}")

##############################################################
# Range Function

total = 0 
for number in range(2, 101, 2):
   total += number
print(total)

##############################################################
# The FizzBuzz

for number in range(1, 101):
   if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
   elif number % 3 == 0:
      print("Fizz")
   elif number % 5 == 0:
      print("Buzz")#   else:
      print(number)