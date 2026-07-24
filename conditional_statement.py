#CONDITIONAL STATEMENTS(NUMBER 1)
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > 0 and b > 0:
    print("a and b are '+'")
elif a > 0 or b > 0:
    print("only one is '+'")
else:
    print("Neither is positive")

    #NUMBER 2
numbers = input("Enter three numbers separated by commas (e.g. 7, 9, 11): ")
parts = numbers.split(",")

x = int(parts[0].strip())
y = int(parts[1].strip())
z = int(parts[2].strip())

if x < y < z:
    print("Increasing order")
elif x > y > z:
    print("Decreasing order")
else:
    print("Neither")

    #NUMBER 3
word = input("Enter a word: ")

if word == word[::-1]:
    print("Is a palindrome")
else:
    print("Not a palindrome")

    # NUMBER-4
x = input("Enter x: ")
y = input("Enter y: ")
z = input("Enter z: ")

if x == y == z:
    print("All same")
elif x == y or y == z or x == z:
    print("Two are equal")
else:
    print("All different")

    # NUMBER-5
angle1 = float(input("Enter angle1: "))
angle2 = float(input("Enter angle2: "))
angle3 = float(input("Enter angle3: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    print("Valid triangle")
else:
    print("Invalid triangle")

    # NUMBER-6
ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

    # NUMBER-7
colors_input = input("Enter three colors separated by commas: ")
color1, color2, color3 = [c.strip().lower() for c in colors_input.split(",")]

primary_colors = ["red", "blue", "yellow"]

if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
    print("All primary colors")
else:
    print("Not all primary colors")

    # NUMBER-8
mode = input("Enter mode: ").lower()

if mode == "manual":
    print("Manual mode activated")
elif mode == "automatic":
    print("Automatic mode activated")
elif mode == "off":
    print("System is off")

    # NUMBER-9
message = input("Enter message: ").lower()

if "urgent" in message or "important" in message or "immediate" in message:
    print("High priority message")
else:
    print("Normal message")

    # NUMBER-10
status1 = input("Enter status1: ").lower()
status2 = input("Enter status2: ").lower()

if status1 == "active" and status2 == "active":
    print("Both active")
elif status1 == "active" or status2 == "active":
    print("One active")
else:
    print("None active")

# NUMBER-11
filename = input("Enter filename that ends with either .png, .jpg or .gif: ")
if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".gif"):
    print("Image file")
else:
    print("Not an image file")

# NUMBER-12
access_level = input("Enter an access_level: ")
if access_level == "admin":
    print("Full access")
elif access_level == "user":
    print("Limited access")
else:
    print("No access")

# NUMBER-13
email_address = input("Enter an email address: ")
if "@" in email_address and "." in email_address:
    print("Valid email")
else:
    print("Invalid email")

# NUMBER-14
day = input("Enter any day of the week: ").lower()
if day == "saturday" or day == "sunday":
    print("Weekend")
elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Weekday")

# NUMBER-15
numbers = input("Enter numbers separated by commas: ")
numbers_infinity = numbers.split(",")
numbers_infinity = [int(n) for n in numbers_infinity]
print(numbers_infinity)

if all(n > 0 for n in numbers_infinity):
    print("It is greater than 0")
else:
    print("It is not greater")#CONDITIONAL STATEMENTS(NUMBER 1)
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > 0 and b > 0:
    print("a and b are '+'")
elif a > 0 or b > 0:
    print("only one is '+'")
else:
    print("Neither is positive")

    #NUMBER 2
numbers = input("Enter three numbers separated by commas (e.g. 7, 9, 11): ")
parts = numbers.split(",")

x = int(parts[0].strip())
y = int(parts[1].strip())
z = int(parts[2].strip())

if x < y < z:
    print("Increasing order")
elif x > y > z:
    print("Decreasing order")
else:
    print("Neither")

    #NUMBER 3
word = input("Enter a word: ")

if word == word[::-1]:
    print("Is a palindrome")
else:
    print("Not a palindrome")

    # NUMBER-4
x = input("Enter x: ")
y = input("Enter y: ")
z = input("Enter z: ")

if x == y == z:
    print("All same")
elif x == y or y == z or x == z:
    print("Two are equal")
else:
    print("All different")

    # NUMBER-5
angle1 = float(input("Enter angle1: "))
angle2 = float(input("Enter angle2: "))
angle3 = float(input("Enter angle3: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    print("Valid triangle")
else:
    print("Invalid triangle")

    # NUMBER-6
ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

    # NUMBER-7
colors_input = input("Enter three colors separated by commas: ")
color1, color2, color3 = [c.strip().lower() for c in colors_input.split(",")]

primary_colors = ["red", "blue", "yellow"]

if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
    print("All primary colors")
else:
    print("Not all primary colors")

    # NUMBER-8
mode = input("Enter mode: ").lower()

if mode == "manual":
    print("Manual mode activated")
elif mode == "automatic":
    print("Automatic mode activated")
elif mode == "off":
    print("System is off")

    # NUMBER-9
message = input("Enter message: ").lower()

if "urgent" in message or "important" in message or "immediate" in message:
    print("High priority message")
else:
    print("Normal message")

    # NUMBER-10
status1 = input("Enter status1: ").lower()
status2 = input("Enter status2: ").lower()

if status1 == "active" and status2 == "active":
    print("Both active")
elif status1 == "active" or status2 == "active":
    print("One active")
else:
    print("None active")

# NUMBER-11
filename = input("Enter filename that ends with either .png, .jpg or .gif: ")
if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".gif"):
    print("Image file")
else:
    print("Not an image file")

# NUMBER-12
access_level = input("Enter an access_level: ")
if access_level == "admin":
    print("Full access")
elif access_level == "user":
    print("Limited access")
else:
    print("No access")

# NUMBER-13
email_address = input("Enter an email address: ")
if "@" in email_address and "." in email_address:
    print("Valid email")
else:
    print("Invalid email")

# NUMBER-14
day = input("Enter any day of the week: ").lower()
if day == "saturday" or day == "sunday":
    print("Weekend")
elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Weekday")

# NUMBER-15
numbers = input("Enter numbers separated by commas: ")
numbers_infinity = numbers.split(",")
numbers_infinity = [int(n) for n in numbers_infinity]
print(numbers_infinity)

if all(n > 0 for n in numbers_infinity):
    print("It is greater than 0")
else:
    print("It is not greater")