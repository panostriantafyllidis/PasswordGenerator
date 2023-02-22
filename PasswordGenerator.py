from cgi import print_environ
import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd

while True:

    print("==============================================")
    print("             PASSWORD GENERATOR               ")
    print("==============================================")
    print()
    # Choose to include numbers and special characters
    min_length = input("Enter the minimum length (type 'exit' to quit): ")
    if min_length.lower() == "exit":
        break
   
    # Action for entering invalid input
    elif not min_length.isdigit():
        print
        print("===>>>  Please enter a valid integer  <<<====")
        print("---------------------------------------------")
    
    # Choose to include numbers and special characters
    else:
        min_length = int(min_length)
        has_number = input("Do you want to have numbers (y/n)? ").lower()
        while has_number != "y" and has_number != "n":
            has_number = input("Please enter 'y' or 'n': ")
            print()
        has_special = input("Do you want to have special characters (y/n)? ").lower()
        while has_special != "y" and has_special != "n":
            has_special = input("Please enter 'y' or 'n': ").lower()
            print()
            print()

        #Password generation
        pwd = generate_password(min_length, has_number == "y", has_special == "y")

        #Output
        print("---------------------------------------------")
        print("              GENERATED PASSWORD             ")
        print("---------------------------------------------")
        print("                " + pwd + "                  ")
        print("---------------------------------------------")
        print()
        print()
        print()
