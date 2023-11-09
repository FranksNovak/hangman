# hangman
import random
from hangman2 import stages
# Generování náhodného slova
words = ["harry", "ronald", "albus", "snape", "hermiona", "draco", "crabbe", "goyle", "hagrid"]
random_word = random.choice(words)


# generování podtržítek
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")

# životy
lives = 6
print(stages[lives])

# vypsání slova s podtržítky v normální podobě
printed_word = ""
for one_letter in hidden_word:
    printed_word += one_letter
print(printed_word)

while "_" in hidden_word:
    guess = input("zadejte hádané písmeno\n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess
        
    # kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    print(f"Počet vašich životů je {lives}")
    if lives == 0:
        print("Prohráli jste!")
        break

    # vypsání slova s podtržítky v normální podobě
    printed_word = ""
    for one_letter in hidden_word:
         printed_word += one_letter
    print(printed_word)

    # kontrola vítězství
    if "_" not in hidden_word:
        print("Vyhráli jste!!!")