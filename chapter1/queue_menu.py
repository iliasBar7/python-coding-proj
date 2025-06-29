import re

queue = []

def enqueue(queue,item):
  queue.append(item)
  print(f"Added {item} to the queue.")

def dequeue(queue):
    if not queue:
        print("List is empty")
    else:
        removed = queue.pop(0)
    print("First item removed from queue:", removed)
   

def print_menu():
  print("1. Insert (enqueue) to queue")
  print("2. Remove (dequeue) from queue")
  print("3. Print queue contents")
  print("4. q/Q for Quit")

def get_choice():
  return input("Please provide your choice ").strip()

def menu():

  while True:
    print_menu()

    choice = get_choice()

    if choice.casefold() == "q":
      print("Exiting program.")
      break
    
    pattern = r'^\d$'
    
    valid_match = re.match(pattern,choice)

    if not valid_match:
      print("invalid input. Please enter a number or q/Q for exit ")
      continue

    choice = int(choice)

    match choice:
      case 1:
        num = input("Please provide a num ").strip()
        
        pattern = r'^\d+$'
    
        valid_match = re.match(pattern,num)
        
        if not valid_match:
          print("Error input must be integer")
          continue
        
        num = int(num)
        enqueue(queue,num)
        
      case 2:
        if queue is not None:  
          dequeue(queue)

      case 3:
        print(queue)

      case _ :
        print("Invalid Input...") 
      
    

  



def main():
  menu()

if __name__ == "__main__":
  main()