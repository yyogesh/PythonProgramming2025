age = 120

if age > 90:
    print("You are too old to party, granny.")
elif age < 0:
    print("You're yet to be born")
elif age >= 18:
    print("You are allowed to party")
else: 
    "You're too young to party"


def switch(lang) :
    if lang == "Javascript":
        print("Javascript is a client-side scripting language")
    elif lang == "Python":
        print("Python is a high-level programming language")
    elif lang == "Java":
        print("Java is a popular programming language")
    else:
        print("Unknown language")

switch("Python")
switch("Java")
switch("Javascript")


lang = input("What's the programming language you want to learn? ")

match lang:
    case "Javascript":
        print("Javascript is a client-side scripting language")
    case "Python":
        print("Python is a high-level programming language")
    case "Java":
        print("Java is a popular programming language")
    case _:
        print("Unknown language")




day = input("Enter the day of the week: ").capitalize()

if day == "Saturday" or day == "Sunday":
    print(f"{day} is a weekend.")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print(f"{day} is a weekday.")
else:
    print("That's not a valid day of the week.")



# Take user input for the day of the week
day = input("Enter the day of the week: ").capitalize()

# Match the day to predefined patterns
match day:
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend.")  # Match weekends
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday.")  # Match weekdays
    case _:
        print("That's not a valid day of the week.")  # Default case



method = "POST"

match method:
    case "GET":
        print("Fetching resource...")
    case "POST":
        print("Creating resource...")
    case "PUT":
        print("Updating resource...")
    case "DELETE":
        print("Deleting resource...")
    case _:
        print("Unsupported HTTP method.")



status_code = 200

match status_code:
    case 200:
        print("Request succeeded.")
    case 404:
        print("Resource not found.")
    case 500:
        print("Server error. Please try again later.")
    case _:
        print("Unknown status code.")