from pyscript import display

display("Seatwork 1", target="titlediv") #literal object

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

display(name, target='namediv')
display(age, target='agediv')
display(height2026, target='heightdiv')
display(student_type, target='studentdiv')
display(countries_now, target='countriesdiv')
display(dictionary, target='dictionarydiv')
display(my_favfruits, target='fruitsdiv')
display(daysoftheweek, target='daysdiv')