last = ", last"

sentence_list = ["Type ", "m. ", "This ", "is ", "your ", "last", " chance."]

displayed_string = " "

def program():
    displayed_string = "".join(sentence_list)
    print(displayed_string)
    sentence_list.insert(-1, last)

def actual_program():
  program()
  userinput = input()
  while userinput != "m":
    program()
    userinput = input()
  print("That's what I thought...")

actual_program()