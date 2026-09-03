from pyscript import display, document

display(f"Welcome to my Seatwork 1", target="titlediv") #literal object

#variable object

name = "Bausa G" # this is astring
age = 15 #this is now an integer
height2026 = 162.56 #now we move on to a float
countries_now = ["Russia", "Malaysia", "Canada"] #this data type is a list
student_type = False #this is a boolean, i am a veteran obmc student
dictionary = {
         "color": "red",
         "car_brand": "Cadillac",
         "shoe_size": "8.5",
         "best_friend": "Jericho",
} #this is a dictionary, many things here

my_favfruits = {"Mango", "Banana", "Lemon", "Blueberry", "Strawberry"} #this data type is a set
daysoftheweek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #this data type is a tuple

display(f"My name is {name}", target='namediv')
display(f"I am currently {age} years old", target='agediv')
display(f"My height is {height2026} cm", target='heightdiv')
display(f"Am I a new student?: {student_type}", target='studentdiv')
display(f"Countries I have visited: {', '.join(countries_now)}", target='countriesdiv')
display(f"Dictionary: {dictionary}", target='dictionarydiv')
display(f"My favorite fruits are: {', '.join(my_favfruits)}", target='fruitsdiv')
display(f"Days of the week: {', '.join(daysoftheweek)}", target='daysdiv')

#below is part 2, calculations

def ze_mathematics(e):
    document.getElementById('output').innerHTML = "" # clears previous output
    num1 = float(document.getElementById('neckhurts').value) # get 1st input
    num2 = float(document.getElementById('aurafarm').value)  # get 2nd input
    sum = num1 + num2 # use operator "+" to add and obtain sum
    difference = num1 - num2 # use operator "-" to subtract and obtain difference
    product = num1 * num2 # use operator "*" to multiply and obtain product
    quotient = num1 / num2 # use operator "/" to divide and obtain quotient

    display(sum, target = 'add') #display sum
    display (difference, target = 'subtract') #display difference
    display (product, target = 'multiply') #display product
    display (quotient, target = 'divide') #display quotient