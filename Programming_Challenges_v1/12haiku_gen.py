# import syllables
# This import can be used to count syllabes in words later

import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Improve this: string should be read from .txt
original_str = 'Ratz was tending bar, his  prosthetic  arm  jerking monotonously  as he filled a tray of glasses with '\
               'draft Kirin. He saw Case and smiled, his teeth a web work of East European steel and brown decay. ' \
               'Case found a place at the bar, between the unlikely tan  on one of Lonny  Zone\'s whores and  the ' \
               'crisp  naval uniform  of a  tall African whose  cheekbones were ridged  with precise rows of  tribal ' \
               'scars. '
vowels = "aeiouy"

print("Amount of words in original string is:", len(original_str.split()))

# Var-counter of vowels in a string. This counter will help if you`ll want
# to improve your haiku making it more close to traditional haiku.
# (5-7-5 pattern and 17 syllables in the whole haiku. Check https://en.wikipedia.org/wiki/Haiku)
counter = 0
# Iteration over all letters in a string
for w in original_str.lower():
    # Comparison between letters and vowels
    for letter in vowels:
        if w == letter:
            counter += 1

print("Amount of syllabes in original string is:", counter)

punct_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(original_str)
filtered_sentence = [w for w in word_tokens if w not in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words and w not in punct_marks:
        filtered_sentence.append(w)

# print("String filtered with NLTK module and punctuation marks:", filtered_sentence)

haiku = "\n" + filtered_sentence[random.randint(0, len(filtered_sentence) - 1)] + " "\
        + filtered_sentence[random.randint(0, len(filtered_sentence) - 1)] + "\n" \
        + filtered_sentence[random.randint(0, len(filtered_sentence) - 1)] + " " + \
        filtered_sentence[random.randint(0, len(filtered_sentence) - 1)] + " " \
        + filtered_sentence[random.randint(0, len(filtered_sentence) - 1)] + "\n" \
        + filtered_sentence[random.randint(0, len(filtered_sentence) - 1)] + " " +\
        filtered_sentence[random.randint(0, len(filtered_sentence) - 1)] + "."

print(haiku)
