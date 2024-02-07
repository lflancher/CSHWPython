from utils.task_6 import text_word_count 

words_in_first_file = 12
words_in_second_file = 7

#Using exec, I am able to create a string that would be a function with the same
#name that is the name of the file (minus txt for ease)
first_file = "Task_6.txt"
first_file = first_file.split(".")[0]
count_first = ("def " + first_file + "():")
count_first += ("\n\tassert text_word_count(" + first_file + ") == ")
count_first += str(words_in_first_file)
count_first += "\n"
exec(count_first)

second_file = "Task_6_Again.txt"
second_file = second_file.split(".")[0]
count_second = ("def " + second_file + "():")
count_second += ("\n\tassert text_word_count(" + second_file + ") == ")
count_second += str(words_in_second_file)
count_second += "\n"
exec(count_second)