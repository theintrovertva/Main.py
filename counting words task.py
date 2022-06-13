file = open("mytextfile.txt", "r")
count = 0
for line in file:
    words = line.split(" ")
    count += len(words)
file.close()
print("Number of Words in the Text File:", count)
