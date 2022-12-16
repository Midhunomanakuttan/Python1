import sys
Myfile = open("myfile.txt", "r")  # opening the file containing the words in read mode
log = open('logfile.txt', 'w')  # opening a file to write the cleaned data in write mode
for x in Myfile: #selecting each word in the file,checks for the erros and bugs
    a_string = x
    alphanumeric = ""
    for character in a_string:
        if character == " ":
            alphanumeric = alphanumeric + character
        elif character.isalnum():
            alphanumeric += character
        elif character == '-':
            alphanumeric = alphanumeric + " "
    log.write(alphanumeric + '\n') # The cleaned data is written into the log file
log.close()
# #making the text file as a list
my_file = open("logfile.txt", "r")
import re
from itertools import permutations
op = set()
my_file = open("logfile.txt", "r")
# reading the file
data = my_file.read()
# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")# The textfile is converted to the list
# print(data_into_list)
for inp in data_into_list:# The main loop which travels through each of the cleaned data
    whitespace = r"\s+"
    short = []
    aftershort = []
    fletter = inp[0]
    lettr = [x.upper() for x in inp]
    for y in list(permutations(lettr, 3)):#fiding the possible permutations of the selected word
        z = "".join(y)
        if len(z) == 3 and z[0] == fletter:
            op.add(z)
            short.append(z)
    for sh in short:
        nospaces = re.sub(whitespace, "", sh)
        aftershort.append(nospaces)
    new_list = [] # getting the list of words after removing the spaces
    for choice in aftershort:
        if choice not in new_list:
            new_list.append(choice)
    original_list = []
    for abb in new_list:
        if len(abb) == 3:
            original_list.append(abb)
    d = {'A': 25, 'C': 8, 'B': 8, 'E': 35, 'D': 9, 'G': 9, 'F': 7, 'I': 25, 'H': 7, 'K': 6, 'J': 3, 'M': 8, 'L': 15,
         'O': 20, 'N': 15, 'Q': 1, 'P': 8, 'S': 15, 'R': 15, 'U': 20, 'T': 15, 'W': 7, 'V': 7, 'Y': 7, 'X': 3, 'Z': 1}
    min_sum = []
    # finding the score of each abbreviation excluding the first letter
    data_inorder = []
    def order(a, b): #finding the permutations which are only in the word sequence
        if len(b) == 0:
            return True
        if len(a) == 0:
            return False
        if (a[0] == b[0]):
            return order(a[1:], b[1:])
        else:
            return order(a[1:], b)
    for i in original_list:
        if __name__ == '__main__':
            m1 = inp.upper()
            m2 = i
            if (order(m1, m2)):
                data_inorder.append(m2)
    for test in data_inorder:
        score = sum(d[c] for c in test[1:])
        for val, item in enumerate(inp):
            y = item.upper()
            for i in test:
                if y == i:
                    if val == 1:
                        score += 1
                    if val == 2:
                        score += 2
                    if val >= 3:
                        score += 3
        min_sum.append(score)
    # # finding the index number of minimum value of the score
    # need to find all the minimum value and its indexes.
    # need to save the abbreviations belong to each of the minimum value
    positions = []
    small = min(min_sum)
    for index, elem in enumerate(min_sum):
        if elem == small:
            positions.append(index)
    repeated = []
    for i in positions:
        repeated.append(data_inorder[i])
    outF = open("omanakuttan_myfile_abbrevs.txt", "a")#opening a file to print the output
    # print(inp)
    outF.write(inp)
    outF.write('\n')
    flag = 0
    for i in repeated:
        length = len(repeated)
        if flag <= length:
            outF.write(i)
            flag = flag + 1
            outF.write('\t')
    outF.write('\n')
    flag = 0
    outF.close()
