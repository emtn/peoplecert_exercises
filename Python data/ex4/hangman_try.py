#ask for the word from one user and give it a value on global scope
from RandomWordGenerator import RandomWord

rw = RandomWord(max_word_size=5)

print(rw.generate())
def get_secret_word():
    word = input("give your secret word\n")
    print(f"the secret word has {len(word)} letters\n{'*'*len(word)}")
    return word

#print each part of the hangman
def print_hangman(wrong_guess):
    if wrong_guess == 1:
        print ('  _\n (_)')
    elif wrong_guess == 2:
        print('  _\n (_)\n  |\n  |')
    elif wrong_guess == 3:
        print('  _\n (_)\n\_|\n  |')
    elif wrong_guess == 4:
        print('  _\n (_)\n\_|_/\n  |  ')
    elif wrong_guess == 5:
        print('  _\n (_)\n\_|_/\n  |  \n_/')
    elif wrong_guess == 6:
        print('  _\n (_)\n\_|_/\n  |  \n_/\_')

#checks if the letter is in the word and prints the word again
def check_letter_in_word(word,letter):
    word_flag=''
    for char in word:
        if letter==char:
            word_flag=word_flag+char
        else:
            word_flag = word_flag+'*'   
    print(word_flag)

secret_word=get_secret_word()
letters_found = ''

def all_letters(word,letters):
    for char in word:
        if char in letters:
            flag=True
        else:
            return False
    return flag
    


print(all_letters('abracadabra','abrcs'))