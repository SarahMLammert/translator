from translate import Translator


def capitalize_first_letter(word):
    return word[0].upper() + word[1:]


_available_languages = {'spanish': 'es', 'portuguese': 'pt',
                        'chinese': 'zh', 'japanese': 'ja', 'korean': 'kor'}
print('Hi! This is a translator from English to any of the following:')
[print(capitalize_first_letter(language))
 for language in _available_languages.keys()]

while True:
    wanted_language = input(
        'The language you want to translate your text to: ').lower()

    if wanted_language.lower() in _available_languages:
        translator = Translator(to_lang=_available_languages[wanted_language])
        break
    else:
        print('Your input was invalid.\nPlease try again.')

try:
    file_name = input(
        'The name of the file you want to translate without the .txt: ')

    with open('./test.txt', mode='r') as original_file:
        text = original_file.read()
        translation = translator.translate(text)

        with open('./test-' + _available_languages[wanted_language] + '.txt', mode='w') as translated_file:
            translated_file.write(translation)

    print(
        f'The text in your original_file was translated to {wanted_language} and put into \'test-' + _available_languages[wanted_language] + '.txt\'')

except FileNotFoundError as e:
    print('Check your file path.')
