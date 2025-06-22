


name = input("Provide your Name")
age = input("Provide your Age")
gender = input("Provide your Gender")
interest = input("Provide your interest")

arr = [name,age,gender,interest]

if  any (not field.strip() for field in arr) :
      print("One or More Fields are empty. Exiting...")
      exit()
else:
  print(f"Hello my name is {name} and Im {age} years old also my gender is {gender} moreover my interest is {interest} ")
