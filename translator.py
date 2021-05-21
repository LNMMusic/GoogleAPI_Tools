from google_trans_new import google_translator, LANGUAGES;  import pyperclip
translator = google_translator()

# BASE INPUT
languages= {
    'es':'Español',     'en':'Ingles',
    'fr':'Frances',     'it':'Italiano',
    'ru':'Ruso',        'sl':'Slovenio',
    'bg':'Bulgaro',     'sr':'Serbiano',
}
text=''
while text!='0':
    # INPUTS
    text = input('Insert Text: ')
    while not text:
        text = input('Insert Text: ')

    if text!='0':
        source=input('Insert Source: ')
        while source not in LANGUAGES:
            source=input('Invalid Source: ')

        # TRANSLATION
        translations = {}
        for lang in languages:
            if lang != source:
                translations[lang]=translator.translate(text, lang_src=source, lang_tgt=lang)

        # FRONT END
        print(f'\n\nOriginal Text:\t{text}\n')

        for key, value in translations.items():
            if key != source:
                print(f'[{key}] {languages[key]}: \t\t{value}')
                # if len(languages[key])<=4:
                #     print(f'[{key}] {languages[key]}: \t\t\t{value}')
                # else:
                #     print(f'[{key}] {languages[key]}: \t\t{value}')
        
        # pyperclip
        selection = input("\nCopy Key-Text: ")
        if selection != '-':
            pyperclip.copy(translations[selection])

        print('___________________________________________________\n\n')