#This is a comment
#This is a print metho.d Print will echo out anything inside the
#() round braceets to the terminal, when we read the file
print("This is my very first python script!!!")

#variables are placeholders, with dynamic values -> things that can change
#they get stored in memory and referenced alter
name = "Tina"
age = 28
eyecolour = "brown"
haircolor = "brown"

#Arrays are variables on steroids. They let us store many values in one
#variables -> to help us group data.
#this makes our scripting files easier to understand and work it.
#car1 = "Toyota"
#car2 = "Volvo"
#car3 = "Fiesta"
cars = ["Toyota", "Toyota", "Fiesta"]

print("My name is" + name)

#input is another Python termm - it waits with a flashing cursor
#until you type something and hit enter
alternativeName = input("What is YOUR name?")

print("My name is now" + alternativeName)

print("My age is " + str(age))
