import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("H A N G M A N")

while True:
    answer = input('Type "play" to play the game, "exit" to quit: ')

    if answer == "exit":
        break
    else:
        word_list = random.choice(('python', 'java', 'kotlin', 'javascript'))
        hidden_word = ['-'] * len(word_list)
        set_of_words = set(word_list)
        complete_word_set = set(word_list)
        used_letters = []

        print()
        life = 8
        while life != 0:
            print(''.join(hidden_word))

            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("You should input a single letter\n")
            elif letter not in letters:
                print("Please enter a lowercase English letter\n")
            elif letter in used_letters:
                print("You've already guessed this letter\n")
            elif letter in set_of_words:
                print()
                for i in [index for index, i in enumerate(word_list)
                          if i == letter]:
                    hidden_word[i] = letter

                set_of_words.remove(letter)
            else:
                life -= 1
                print("That letter doesn't appear in the word\n" if life > 0
                      else "That letter doesn't appear in the word")

            if '-' not in hidden_word:
                print(''.join(hidden_word),
                      "\nYou guessed the word!\nYou survived!\n")
                break
            elif life == 0:
                print("You lost!\n")

            used_letters.append(letter)
