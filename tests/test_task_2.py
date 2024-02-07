#Calling the function from the file
from utils.task_2 import Ness, Paula, Jeff, Poo

#This function tests if the variable found in the "Ness" function is an integer
def test_ness():
  
  assert isinstance(Ness(), int) == True

#This function tests if the variable found in the "Paula" function is a float
def test_paula():
  assert isinstance(Paula(), float) == True 

#This function tests if the variable found in the "Jeff" function is a string
def test_jeff():
  assert isinstance(Jeff(), str) == True 

#This function tests if the variable found in the "Poo" function is a bool
#Poo is the name of the fourth party member in Earthbound.
def test_poo():
  assert isinstance(Poo(), bool) == True
