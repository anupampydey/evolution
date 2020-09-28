import string
from random_words import RandomWords


def main_display():
    while True:
        print('What do you want to do?')
        print('a) Prints random words having 100% score')
        print('b) Check the score value of your word')
        print('q) Quit the program')
        option = input('Please choose the correct option (a/ b/ q) >')
        print()
        if option == 'a':
            rand_words()
        elif option == 'b':
            word_score()
        elif option == 'q':
            print("Thanks for using this program!!")
            break
        else:
            print("Error!! Please choose a correct option\n")


def word_score():
    word = input('Please enter the english word >')
    print()
    score = 0
    if word.isalpha():
        word = word.upper()
        for ch in word:
            score += alpha_value[ch]
    else:
        print('Error!! This is not an english word.\n')
        return
    print(word, '=', score, '\n')

def rand_words():
    perfect = []
    rw = RandomWords()
    f = input('Enter the first alphabet of word or press enter for all words >').strip()
    print()
    for n in range(10000):
        score = 0
        if f and f.isascii():
            word = rw.random_word(f).upper()
        else:
            word = rw.random_word().upper()
        for ch in word:
            if ch in alpha_value.keys():
                score += alpha_value[ch]
        if score == 100 and word not in perfect:
            perfect.append(word)
    print('Random words with 100% score value are as listed below:')
    for ch in up_alp:
        subword = []
        for word in perfect:
            if word.startswith(ch):
                subword.append(word)
        if subword:
            print(f'Word starting with "{ch}" are:')
            print(subword)
            print()
    print()


# Main Body
print("""The program calculates the perfect words from English Dictionary whose value is equal to 100
e.g. if A=1, B=2, C=3 and ... Z=26 then 'ARRIVALS = 100'
""")
alpha_value = {}
up_alp = list(string.ascii_uppercase)
for i, cha in enumerate(up_alp):
    alpha_value[cha] = i+1
main_display()
