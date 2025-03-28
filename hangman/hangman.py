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
print('\n')
print('\n')
print('Welcome to the Humgman game if you Guess the word correctly you save the life\n')
lives = len(stages)
Dictionary = open("E:\codes\python\projects\hangman\words.txt",'r')
words = Dictionary.readlines
words = [word.strip() for word in Dictionary]
chosen_word = random.choice(words)
word_length = len(chosen_word)
end = False
Display = []
for letter in chosen_word:
    Display += '_'
print(Display) 
i = 0
while not end:
    Guess = input('Guess the letter: ').lower()
    for position in range(0,word_length):
        letter = chosen_word[position]
        if Guess == letter:
            Display[position] = Guess
    if Guess not in chosen_word:
      lives -=1
      if lives == 0:
        print(stages[0])
        print('You lose')
        print(f"The word is {chosen_word}")
        break
      else:
        print(stages[lives])
    print(Display)
    if '_' not in Display:
        end = True
        print('You win')