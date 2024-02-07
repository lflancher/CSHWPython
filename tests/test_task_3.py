from utils.task_3 import prime, ispositive, allnumbers


#For all of these function, Pytest is most cooperative in replit when there is 
#an endline character 

#For all of these functions, I took advantage of pytest's ability to read output

#I looked up the first few prime numbers in order to guarentee my function was right

def test_prime(capfd):
  prime()
  out, err = capfd.readouterr()
  assert out == (str([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) + "\n")

#I tested the number "2" to ensure that it was Positive
def test_ispositive(capfd):
  ispositive(2)
  out, err = capfd.readouterr()
  assert out == "Positive\n"

#I tested the number "-2" to ensure it was negative
def test_isnegative(capfd):
  ispositive(-2)
  out, err = capfd.readouterr()
  assert out == "Negative\n"

#I tested zero
def test_iszero(capfd):
  ispositive(0)
  out, err = capfd.readouterr()
  assert out == "Zero\n"

#I asked Google to find 5050
def test_allnumbers(capfd):
  allnumbers()
  out, err = capfd.readouterr()
  assert out == (str(5050) + "\n")