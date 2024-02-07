def ispositive(z):
  #Taking the z as an argument and finding if it's positive, negative or equal to zero
  if z > 0:
    print("Positive")
  elif z < 0:
    print("Negative")
  else:
    print("Zero")

def prime():
  #So this is calculating a prime number
  #Essentially it takes a number if it is divisible by 2, 3, 5 or 7 and also not equal to those numbers
  primen = []
  for i in range (2, 100):
    if i > 1:
      if (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and (i % 5 != 0 or i == 5):
        if (i % 7 != 0 or i == 7):
          primen.append(i)
    if (len(primen) == 10):
      break
  print(primen)

#Using a while loop, iterating the loop everytime until the number is 100,
#and then adding each of those numbers to another integer and at the end printing
#that integer
def allnumbers():
  i = 0
  j = 0
  while (i <= 100):
    j = j + i 
    i = i + 1
  print(j)
  