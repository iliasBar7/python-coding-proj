

# Python Functions 
def get_input(prompt):
    value = input(prompt)
    if not value.strip() :
        print("input cannot be empty or contains spaces. Exiting....")
        exit()
        return value

name = get_input("Provide your Name: ")
age = get_input("Provide your Age: ")
gender = get_input("Provide your Gender: ")
interest = get_input("Provide your interest: ")

print(f"Hello my name is {name} and Im {age} years old also my gender is {gender} moreover my interest is {interest} ")




        