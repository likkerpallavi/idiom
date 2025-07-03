from googletrans import Translator

def translate_to_telugu(word):
    translator = Translator()
    result = translator.translate(word, src='en', dest='te')
    return result.text

def main():
    english_word = input("Enter an English word: ")
    telugu_meaning = translate_to_telugu(english_word)
    print(f"The meaning of '{english_word}' in Telugu is: {telugu_meaning}")

if __name__ == "__main__":
    main()
