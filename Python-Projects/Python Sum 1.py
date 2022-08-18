import re
find_word = input('What Character do you want to see ? :   ')
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
find_word.lower()
first_letter_of_searched_word = find_word[0]
name_list = []
for num in nums:
    if num in find_word:
        print('Unfortunately,  there is a number in this Name, try again.')
        exit()

with open("C:\Andre-Projects\Python-Projects\Characters.txt", "r") as char_book:
    # print(char_book.read())
    for line in char_book:
        i = line.find(':')
        name = line[0:i]
        name_list.append(name)
        # print(dict_list)
        if find_word == name:
            print(line[i+1:])
            exit()
print('Not Found')
if input('Want Closest Match?  Y/N  ').lower() == 'y':
    for word in name_list:
        if re.search(first_letter_of_searched_word+'+', word):
            print(word)


# ==============================================================================================
