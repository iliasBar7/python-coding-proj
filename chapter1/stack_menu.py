
stack= []

def push(list, item):
  list.append(item)


def pop(list):
    if not list:
      return "Stack is empty"
    else:
      return list.pop()
    

def get_choice():
  return input("Please provice a choice \n")



def get_menu():
   print("1.Insert on top")
   print("2. Get from top")
   print("3. Print stack")
   print("4. q\Q for Quit")


while True:
  get_menu()
  choice = get_choice()
  

  if not choice: 
    continue

  if choice.casefold() == "q": 
    break

  

  choice = int(choice)
  
 

  # pattern = r"^\d$"

  # valid = re.match(pattern,choice)

  

  # if not valid:
  #   print("Please provide a valid input ")
  #   continue

  match choice:
    case 1:
     try:
      num = int(input("Please insert a num ").strip())
      
      push(stack,num)
      print("Product added Successfully")
      # print(f"Debug {product_stack}")
     except ValueError:
       print(f"Invalid input..{num} must be integer ")

    case 2:
      out_num = pop(stack)
      if out_num is not None:
        print("Item pop:",out_num)

    case 3:
      print(stack)
    
    case _:
      print("Invalid input...")

        
       

