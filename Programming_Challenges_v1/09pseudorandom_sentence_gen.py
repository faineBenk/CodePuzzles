import re
# import os
import random

# how to resolve path-problem?
file = open("C:\\Users\\stank\\PycharmProjects\\CodePuzzles\\Programming_Challenges_v1\\sources\\sentences.txt")
text = ''.join(file.readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

# print(os.getcwd())
print(random.choice(sentences) + ".")
