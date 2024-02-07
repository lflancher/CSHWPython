import pandas

#I used the pandas library and while it is traditional to import pandas as pd,
#I skipped that for this assignment for the sake of ease of grader.

def the_sum(numbers):
  #There's no need to explain the entirety of Panda's usefulness so I'll just say
  #that I took a list and made it a series and used Panda's sum function. I could've 
  #gone crazy and read a CSV file or something but all I needed to prove was that I 
  #could import the package
  print(pandas.Series(numbers).sum())