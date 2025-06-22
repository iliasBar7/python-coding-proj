s = "Coding Factory"

found = False

for i in range(len(s)):
  if "C" in s:
    print(f"We found C in: {s} ")
    found = True
    break
  if not found:
    print("we dont find it")
   

for i in range(len(s)):
  print(s[::-1]) 
  break
   
  
  # print(s[i], end= '')

#   print()

# for char in s:
#     print(char)