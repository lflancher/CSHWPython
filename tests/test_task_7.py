from utils.task_7 import the_sum

#I used the pandas library here

def test_the_sum(capfd):
  numbers = [1, 2, 3, 4, 5]
  the_sum(numbers)
  out, err = capfd.readouterr()
  assert out == (str(15) + "\n")

def Test_the_sum(capfd):
  numbers = [2, 3, 4, 12]
  the_sum(numbers)
  out, err = capfd.readouterr()
  assert out == (str(21) + "\n")

def Test_The_sum(capfd):
  numbers = [50, 12, 67, 3]
  the_sum(numbers)
  out, err = capfd.readouterr()
  assert out == (str(132) + "\n")