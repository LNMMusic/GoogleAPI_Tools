from googlesearch import search
from google_trans_new import LANGUAGES

import pyperclip

text = '';    amount = 0;    lang = ''

while text!='0':
    # INPUTS
    text = input('Search: ')
    while not text:
        text = input('Search: ')
    if text != '0':

        lang=input('Language: ')
        while lang not in LANGUAGES:
            lang=input('Invalid Language: ')

        amount=int(input('Amount: '))
        while amount == 0:
            amount=int(input('Amount: '))

        # SEARCHING
        results = search(text, num_results=amount, lang=lang)

        # FRONT-END
        print('\n\n')
        for ix, value in enumerate(results):
            print(f'{ix}. {value}')

        # pyperclip
        selection = input("\nCopy Web ['-' to not]: ")
        if selection != '-':
            pyperclip.copy(results[int(selection)])

        print('___________________________________________________\n\n')