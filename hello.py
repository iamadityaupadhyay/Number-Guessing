import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
name=["aditya","kajal"]
display=[]
choosen_word=random.choice(name)
print(f"The choosen word is {choosen_word}")
for i in range(len(choosen_word)):
    display+="_"
# user_letter=input("Guess the letter:").lower()
# for i in range(len(choosen_word)):
#     letter=choosen_word[i]
#     if letter==user_letter:
#         display[i]=user_letter
j=6
for i in range(len(choosen_word)):
    user_letter=input("Guess the letter:").lower()
    letter=choosen_word[i]
    if letter==user_letter:
        display[i]=user_letter
    print(display) 
    print(stages[j])
    j-=1
for i in range(len(choosen_word)):  
        if display[i]==choosen_word[i]:
            flag=1
        else:flag=2
if flag:print("You win")
else:print("You lose")