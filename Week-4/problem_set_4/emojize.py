# Problem Set 4 - Emojize

#pip3 install emoji

import emoji

text = input("Input: ")

print(f"Output: {emoji.emojize(text, language = "alias")}")
    