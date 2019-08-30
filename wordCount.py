import os
import sys

file = open(str(sys.argv[1]), "r")
#Replaces the special characters by an empty string symbol.
#The string is divided by spaces.
file_as_string = file.read().replace('.', "").replace(",","").replace(";","").replace(":","").replace("\n"," ").replace("\"", "").replace("-"," ").replace("'"," ").split(" ")

word_dict = {}

#This allows to intialize every entry in the dictionary as 0.
#In addition the if statement prevents to introduce the empty string symbol to the dictionary. 
for word in file_as_string:
    if not str(word) == '':
        word_dict[str(word).lower()] = 0

#For every entry of a word the value of the key-value pair associated with the word gets added 1.
#The empty string symbol is ignored.
for word in file_as_string:
    if not str(word) == '':
        word_dict[str(word).lower()] += 1

#The list is sorted by the natural order of the keys which is alphabetical
word_sorted_keys = sorted(word_dict.keys())

output = open(str(sys.argv[2]), "w")

#A list to check the output of the program is printed.
#The same list of words and each word's repetitions are added to a file.
for key in word_sorted_keys:
    print("Entry:",str(key),"||||||","Repeats:",word_dict[key])
    output.write(str(key)+" "+str(word_dict[key])+"\n")
file.close()
output.close()
