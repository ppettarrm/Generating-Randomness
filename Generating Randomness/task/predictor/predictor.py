import random

MIN_LEN = 100
print("Please provide AI some data to learn...\nThe current data length is 0, 100 symbols left")
print("Print a random string containing 0 or 1:\n")
input_string = input()

i = 0
result_string = ""
while True:
    for iterator in input_string:
        if iterator == '0' or iterator == '1':
            result_string += iterator
    if len(result_string) < MIN_LEN:
        print(f"Current data length is {len(result_string)}, {MIN_LEN - len(result_string)} symbols left")
        print("Print a random string containing 0 or 1:\n")
        input_string = input()
    else:
        break

print("\nFinal data string:")
print(result_string + "\n")

tokens = ["000", "001", "010", "011", "100", "101", "110", "111"]
final_list = [result_string[iterator:iterator + 4] for iterator in
              range(0, len(result_string) - 3)]  # Adjusted the range to get substrings of length 3.
output = {key: [0, 0] for key in tokens}

for substring in final_list:
    key = substring[0:-1]  # Removed the slicing to match the length of the keys in the dictionary.
    if substring[-1] == '1':  # Adjusted the slicing to get the last character.
        output[key][1] += 1
    else:
        output[key][0] += 1

money = 1000

print(
    'You have $1000. Every time the system successfully predicts your next press, you lose $1.\nOtherwise, '
    'you earn $1. Print "enough" to leave the game. Let\'s go!\n')

while True:
    over = False
    while True:
        print("Print a random string containing 0 or 1: \n")
        test_string = input()
        if test_string == "enough":
            print("Game over!")
            over = True
            break
        if len(test_string) > 3:
            break
    if over:
        break

    test_list = [test_string[iterator:iterator + 4] for iterator in range(0, len(test_string) - 3)]

    guessed = 0
    predicted_string = ""

    for i in range(3):
        predicted_string += str(int(random.random()))

    for substring in test_list:
        key = substring[:-1]
        zeros = output[key][0]
        ones = output[key][1]
        if zeros > ones:
            predicted_string += '0'
        elif ones > zeros:
            predicted_string += '1'
        else:
            predicted_string += str(int(random.random()))
    predicted_string = predicted_string[3:-1]
    for i in range(len(predicted_string)):
        if predicted_string[i] == test_string[i]:
            guessed += 1

    acc = round(guessed / (len(predicted_string) + 1) * 100, 2)
    print(f"predictions:\n{predicted_string}")
    print(f"Computer guessed {guessed} out of {len(predicted_string) + 1} symbols right ({acc} %)")
    money -= guessed
    money += len(predicted_string) + 1 - guessed
    print(f"Your balance is now ${money}")
