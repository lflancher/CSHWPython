def text_word_count(File_Name):
  with open(File_Name, "r") as f:
    return(len(f.read().split()))