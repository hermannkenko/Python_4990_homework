#Homework 4: Write a function that decodes a message from a text file.
#  The text file will contain a list of numbers and words. The numbers represent the position of the word in a pyramid structure.
#  The function should read the text file and return the decoded message.
# Author: Hermann Kenko Tanfoudie
# Date: 03/04/2025

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Parse the numbers and words into a dictionary
    word_dict = {}
    for line in lines:
        num, word = line.strip().split()
        word_dict[int(num)] = word

    # Determine the pyramid structure
    index, level = 1, 1
    selected_numbers = []
    
    while index in word_dict:
        selected_numbers.append(index)
        level += 1
        index += level  # The last number of each row in the pyramid

    # Construct the decoded message
    decoded_message = " ".join(word_dict[num] for num in selected_numbers)
    return decoded_message

# Example usage:
# Assuming the text file is named "message.txt" and is in the same directory as this script
decoded_text = decode("message.txt")
print(decoded_text)
