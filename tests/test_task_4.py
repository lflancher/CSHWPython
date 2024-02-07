from utils.task_4 import calculate_discount

#I tested both floats and integers with this function to ensure my function could work
#with both without me needing to which data type was being worked with


def test_calculate_discount(capfd):
  calculate_discount(100, 10)
  out, err = capfd.readouterr()
  assert out == (str(90.0) + "\n")

def Test_calculate_discount(capfd):
  calculate_discount(100, 20)
  out, err = capfd.readouterr()
  assert out == (str(80) + "\n")

def test_Calculate_discount(capfd):
  calculate_discount(100, 12.5)
  out, err = capfd.readouterr()
  assert out == (str(87.5) + "\n")
