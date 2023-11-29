import random
from colorama import just_fix_windows_console, Fore  #pip install colorama
just_fix_windows_console()

tries = 0

wordFile = open(file="words.txt").read()
words = wordFile.split("\n")

guessword = random.choice(words)

outputFinal = ""

print(f'''{Fore.YELLOW}   ___                          __
  / _ \\__ ________ ___ ________/ /
 / , _/ // (_-<_ // _ `/ __/ _  /
/_/|_|\\_, /___/__/\\_,_/_/  \\_,_/
     /___/
{Fore.CYAN}            ________                __ __
            |  |  |  |.-----.----.--|  |  |.-----.
            |  |  |  ||  _  |   _|  _  |  ||  -__|
            |________||_____|__| |_____|__||_____|
''')

while True:
    outputFinal = ""
    text = input(f"{Fore.WHITE} :3 > ").lower()

    if len(text) != len(guessword):
        print(f"Please enter a {len(guessword)} letter word")
        continue

    if guessword == text:
        print("You win")
        break

    tries = tries + 1

    for i in range(len(text)):

        if text[i] == guessword[i]:
            outputFinal = outputFinal + f"{Fore.GREEN}{text[i]}"

        elif text[i] in guessword:
            outputFinal = outputFinal + f"{Fore.YELLOW}{text[i]}"

        else:
            outputFinal = outputFinal + f"{Fore.WHITE}{text[i]}"

    print(outputFinal)

    if tries >= 6:
        print(f"{Fore.RED}You lose{Fore.WHITE}")
        break

print("word :", guessword)
input()