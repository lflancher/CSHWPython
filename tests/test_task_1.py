#Calling the function from the file.
from utils.task_1 import message 

def test_task_1(capfd):
  #Calling the function, using the capfd which will capture the output, it's included with pytest
  message()
  #out captures the output, while err captures something else that is not the output, I have it there just in case
  out, err = capfd.readouterr()
  #Something about Python or replit that is weird is that testing is most accurate when it gauges a endline character
  assert out == "Hello, Replit!\n"