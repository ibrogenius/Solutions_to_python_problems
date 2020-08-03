# fun project one
def capital_index(string):
    list_num = []
    for i, j in enumerate(string):
        if j.isupper():
            list_num.append(i)
    return list_num


print(capital_index("HeLLo"))

# getting the middle number
message = input('Enter a word: ')
msgLength = int(len(message)/2)
if msgLength % 2 == 0:
    aphabetOne = message[:msgLength]
    alphabetTwo = message[msgLength]
    alphabetThree = message[msgLength:]
    print(f"The middle number is '{alphabetTwo}'")

else:
    print('Oops no middle number')

# getting the middle number using a function
def mid(message):
    msg_length = int(len(message) / 2)
    if msg_length % 2 == 0:
        aphabet_one = message[:msg_length]
        alphabet_two = message[msg_length]
        alphabet_three = message[msg_length:]
        print(f"The middle number is '{alphabet_two}'")
    else:
        print(f'{message} does not contain a middle number. :)')


messages = input('Enter something: ')
mid(messages)

#smiley
input_msg = input('Enter your Welcome message: ')
words = input_msg.split(' ')
emoji = {
    ':)': '...Smiles',
    ':(': 'Sad'
}
final_ouput = ''
for item in words:
    final_ouput += emoji.get(item, item) + ' '

print(final_ouput)

# A game
import random
random = random.randint(1, 10)
while True:
    msg = int(input('Enter a Number: '))
    if msg == random:
        print('You won the game')
        break
    else:
        print('Try again')

# A game 
import random
random = random.randint(1, 10)
num_count = 0
while num_count < 3:
    msg = int(input('Enter a Number: '))
    num_count += 1
    if msg == random:
        print('You won the game')
        break
    else:
        print('Try again')
print('\nYour time is up')

# To get the Largest number in a list
numbers = [1, 2, 3, 4, 7, 9, 10, 6]
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)

# To get the Largest number using a method
def my_num(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    print(max_num)


numbers = [1, 3, 9, 10, 4]
my_num(numbers)

# Easiest way to roll a dice using python
import random
first = random.randint(1, 6)
second = random.randint(1, 6)
print('The dice has been rolled :)\n')
print(f'({first}, {second})')

# Rolling a dice with a bit of Sauce
import random

class randomValue:
    def random_dice(self):
        first_roll = random.randint(1, 6)
        second_roll = random.randint(1, 6)
        if first_roll == 6 and second_roll == 6:
            print(f"You've won the game")
        return first_roll, second_roll


Random = randomValue()
print(Random.random_dice())

#using zip
ask_question = ['name', 'department', 'favorite color', 'favorite food']
answers = ['Inu John', 'CSC', 'Red', 'nothing']
for ask, ans in zip(ask_question, answers):
    print(f"What is your {ask}? {ans}")

# fomatting numbers
dictt = {"Praise": 23, "Ivanka": 23, "Uddin": 23, "Mr. Frodo": 23}
for i, j in dictt.items():
    print(f"{i:10} scores {j:10d}")

