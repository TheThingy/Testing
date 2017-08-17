
def reverse_string(string_input):
    split_string = string_input.split(" ")
    return print(list(reversed(split_string)))

user_input = str(input("Please enter a string with more than 2 words: \n"))

reverse_string(user_input)