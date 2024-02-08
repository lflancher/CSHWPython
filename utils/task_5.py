books = ["The Stand by Stephen King", "The Count of Monte Cristo by Alexandre Dumas", "The Shining by Stephen King", "Infinite Jest by David Foster Wallace", "Fahrenheit 451 by Ray Bradbury","Dune by Frank Herbert"]

student_dict = {
  1 : "Hal",
  2 : "Orin",
  3 : "Mario",
  4 : "Leo",
}

#Using list splicing and printing the new list
def book_list():
  for i in range(0, len(books)):
    books[i] = books[i].split(" by ")[0]
  new_list = books[0:3]
  print(new_list)
  #return new_list

#Taking the student number as an argument and using it to find
#the corresponding student
def people(student_num):
  #return student_dict[student_num]
  print(student_dict[student_num])
