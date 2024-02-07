def text_word_count(File_Name):
  with open(File_Name, "r") as f:
    print(len(f.read().split()))