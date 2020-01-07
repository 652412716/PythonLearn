message = input("Tell me something, and I will repeat it back to you:")
print(message)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
prompt += "\nPlease tell me something: "
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
    else:
        print("program is quit")




