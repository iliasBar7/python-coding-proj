grades = [1,2,3,4,5,6,7,8]

#Append
grades.append (10)

#Update
grades[0] = 15


#delete
grades.remove(2)

# Search with value
if (4 in grades) :
  print(4, "was found")

if(10 in grades):
  positionToUpdate = grades.index(10)

  grades[positionToUpdate] = 7

  print(grades)

#min_value = grades[0]


#Find the min value of grades
# for item in grades:

#     if item < min_value:
#        min_value = item
#        print(min_value)

max_value = grades[0]
       
for item in grades:
    if item > max_value:
      max_value = item 
     
print(max_value)   

           




  
