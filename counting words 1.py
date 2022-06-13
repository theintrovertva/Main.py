from itertools import count


sentence = input ("enter sentence")
count = 0
for line in sentence:
    words = line.split(" ")
    count = len(words)
print("Number of words in the sentence:", count)