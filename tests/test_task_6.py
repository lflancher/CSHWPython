from utils.task_6 import text_word_count 

words_in_file = 12

def test_text_word_count(capfd):
  #I made the file name the argument to ease things up
  text_word_count("test_file.txt")
  out, err = capfd.readouterr()
  assert out == (str(words_in_file) + "\n")