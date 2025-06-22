from cerberus import Validator

def get_input(prompt) :
    value = input(prompt)
    if not value.strip() :
        raise ValueError("input value must not be empty or contains spaces")
       
   # print(f"DEBUG: got input '{value}'")
    return value
    

schema = {
    'name': {'type': 'string', 'minlength': 3},
    'email': {'type':'string', 'regex': r'^[\w\.-]+@[\w\.-]+\.\w+$'},
    'password': {'type':'string',  'regex': r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'}
}

v = Validator(schema)
try:
  user = {
    'name': get_input("Name: "),
    'email': get_input("Email: "),
    'password': get_input("Password: ")
}
except ValueError as e:
  print("Error", e)
  exit()

#print("DEBUG: user dictionary:", user)
if not v.validate(user) : 
    print("Validation errors ",v.errors)
  
else:
  print("Success Authenticated")