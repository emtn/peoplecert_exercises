def print_hangman(wrong_guess):
    if wrong_guess == 6:
        print ('  _\n (_)')
    elif wrong_guess == 5:
        print('  _\n (_)\n  |\n  |')
    elif wrong_guess == 4:
        print('  _\n (_)\n\_|\n  |')
    elif wrong_guess == 3:
        print('  _\n (_)\n\_|_/\n  |  ')
    elif wrong_guess == 2:
        print('  _\n (_)\n\_|_/\n  |  \n_/')
    elif wrong_guess == 1:
        print('  _\n (_)\n\_|_/\n  |  \n_/\_')

def all_letters(word,letters):
    for char in word:
        if char in letters:
            flag=True
        else:
            return False
    return flag

def get_secret_word():
    word = input("give your secret word\n")
    print(f"the secret word has {len(word)} letters\n{'*'*len(word)}")
    return word

def print_word(secret_word,letters_found):



secret_word =  get_secret_word( )
letters_found = ""
tries = 6
found = False 
while   tries > 0  and not  found :
    letter = input( "Μάντεψε ένα γράμμα  : " )
    #print_word(secret_word, letters_found)
    if letter not in secret_word:
        tries  = tries -1
        print_hangman( tries )
    else :
        letters_found += letter
        found = all_letters(secret_word, letters_found )
        print_word(secret_word, letters_found)
        print()
        if found :
            print( "Συγχαρητήριακέρδισες" )