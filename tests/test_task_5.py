from utils.task_5 import book_list, people

def test_book_list(capfd):
  book_list()
  #Replit gave me some trouble with my line size when programming, hence why there is a list that appends new books
  whatiscorrect = ["The Stand"]
  whatiscorrect.append("The Count of Monte Cristo")
  whatiscorrect.append("The Shining")
  out, err = capfd.readouterr()
  assert out == (str(whatiscorrect) + "\n")

def test_people(capfd):
  people(3)
  out, err = capfd.readouterr()
  assert out == ("Mario" + "\n")

def Test_people(capfd):
  people(4)
  out, err = capfd.readouterr()
  assert out == ("Leo" + "\n")

def Test_People(capfd):
  people(1)
  out, err = capfd.readouterr()
  assert out == ("Hal" + "\n")