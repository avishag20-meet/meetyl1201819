####problem 1-
#import tkinter as tk
#from tkinter import simpledialog
##Then when ever you want to ask the user for input use this code
#greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
#if greeting in ("Arrr!"):
#	print("Go away, pirate.")
#else:
#	print("Greetings, hater of pirates!")

####problem 2-
#import tkinter as tk
#from tkinter import simpledialog

#year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

#if year <= 1900:
#    print ("Woah, that's the past!")
#elif year > 1900 and year < 2020:
#    print ("That's totally the present!")
#    print ("Far out, that's the future!!")

####problem 3-
#class Person (object):
# def __init__(self, first_name, last_name):
#    self.first = first_name
#    self.last = last_name
#  def speak(self):
#  	print("My name is " + self.first + " " + self.last)

#me = Person("Brandon", "Walsh")
#you = Person("Ethan", "Reed")

#me.speak()
#you.speak()






####problem 4-
#import tkinter as tk
#from tkinter import simpledialog
## Calculating Grades (ok, let me think about this one)

## Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

## Average	Grade
## 90+	A
## 80-89	B
## 70-79	C
## 60-69	D
## 0-59	F

## Exams: 89, 90, 90
## Average: 90
## Grade: A
## Student is passing.

## Exams: 50, 51, 0
## Average: 33
## Grade: F
## Student iis failing.

#exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))
                                                                         
#exam_two = int(simpledialog.askstring( "Input" , "exam grade two: ", parent=tk.Tk().withdraw()))

#exam_three = int(simpledialog.askstring("Input" , "exam grade three: ", parent=tk.Tk().withdraw()))


#grades = [exam_one, exam_two, exam_three]
#sum = 0
#for grade in grades:
#  sum = sum + grade

#avg = sum / len(grades)

#if avg >= 90:
#    letter_grade = "A"
#elif avg >= 80 and avg < 90:
#    letter_grade = "B"
#elif avg > 69 and avg < 80:
#    letter_grade = "C"
#elif avg <= 69 and avg >= 65:
#    letter_grade = "D"
#else:
#    letter_grade = "F"

#for grade in grades:
# print("Exam: " + str(grade))

#  print("Average: " + str(avg))

#   print("Grade: " + letter_grade)

#if grade is "F":
#    print ("Student is failing.")
#else:
#    print ("Student is stupid.")










####problem 5-
#class Person(object):
#   def __init__(self, name, favorite_food, age, color):
#       self.name = name
#       self.favorite_food = favorite_food
#       self.age = age
#       self.color = color

#   def print_info(self):
#       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
#       print("My favorite food is " + self.favorite_food + " and my favorite color is " + self.color)


#a = Person("Britney", "Pizza", 16, "red")
#a.print_info()

#b = Person("Jake", "banana", 15, "black")
#b.print_info()

####problem 6-
#class Bear(object):
#	def __init__(self, name):
#		self.name = name
#	def created(self):	
#		print("A new bear created. Its name is " + self.name)
	
#	def say_hi(self):
#		print("Hi! I’m a bear. My name is" + self.name)

#my_bear = Bear( " danny")
#my_bear.say_hi()

####problem 7-
#class person(object):
#	def __init__(self, name, balloons, color):
#		self.name = name
#		self.balloons = balloons
#		self.color = color
#	def stupid(self):
#		print("This is a tale about " + str(self.balloons) + " balloons. The first kid is " + self.name + " who got a " + self.color + " balloon")

#r = person ("Ron", 5, "yellow")
#r.stupid()