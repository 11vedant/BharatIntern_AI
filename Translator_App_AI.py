#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install googletrans==4.0.0-rc1')
from googletrans import Translator, LANGUAGES

def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None

def translate_text(input_text, dest_lang_code):
    translator = Translator()
    translated = translator.translate(input_text, dest=dest_lang_code)
    return translated.text

def main():
    print("Language Translator by Vedant Trivedi")

    language_names = list(LANGUAGES.values())
    print("Supported Languages:")
    for index, name in enumerate(language_names, start=1):
        print(f"{index}. {name}")

    while True:
        input_text = input("\nEnter text to translate (type 'exit' to quit): ")
        
        if input_text.lower() == 'exit':
            break

        dest_lang_name = input("Enter the destination language: ")
        dest_lang_code = get_language_code(dest_lang_name)

        if dest_lang_code:
            translated_text = translate_text(input_text, dest_lang_code)
            print(f"Translated text: {translated_text}")
        else:
            print("Invalid destination language. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




