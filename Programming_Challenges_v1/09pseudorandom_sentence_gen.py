import re
import os
import random


for cur_dir, subdirs, files in os.walk("C:"):
    for file in files:
        if file.endswith(".txt"):
            # print("You`ve found the text file.")
            file = open(os.path.abspath("../Programming_Challenges_v1/sources/sentences.txt")
            # print("You`ve opened the text file.")
            text = ''.join(file.readlines())
            sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
            print(random.choice(sentences) + ".")
            break


