import os
import sys

print("Hello World.")
print(sys.argv[1])

print(sys.argv[2])

file = open(str(sys.argv[1]), "r")
file_as_string = file.read().replace('.', "").replace(",","").replace(";","").replace(":","").replace("\n"," ").replace("\"", "").replace("-"," ").replace("'"," ").split(" ")

word_dict = {}

for word in file_as_string:
    if not str(word) == '':
        word_dict[str(word).lower()] = 0

for word in file_as_string:
    if not str(word) == '':
        word_dict[str(word).lower()] += 1

word_sorted_keys = sorted(word_dict.keys())

output = open(str(sys.argv[2]), "w")

for key in word_sorted_keys:
    print("Entry:",str(key),"||||||","Repeats:",word_dict[key])
    output.write(str(key)+" "+str(word_dict[key])+"\n")
file.close()
output.close()
