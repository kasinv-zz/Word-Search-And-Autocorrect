
"""
function to run through all possible options(found, drop swap, replace)
inputs: dictionary, list of word
outouts: result
"""
def found_word(dic_set, input_list_idx):
    #sees if word is in dictionary as is
    if input_list_idx in dic_set:
        return input_list_idx, "FOUND"
    else:
        """
        goes through all possible combinations of dropped letter in word
        checks to see if it is in the dictionary
        """
        letter_list = list(input_list_idx)
        for i in range(len(letter_list)):
            letter_list = list(input_list_idx)
            word = ""            
            letter_list.pop(i)
            word = ''.join(letter_list)
            if word in dic_set:
                return word, "DROP"
            else:
                continue
        else:
            """
            goes through all possible swap letter combinations
            checks to see if that word is in the dictionary
            """
            letter_list = list(input_list_idx)
            for i in range(len(letter_list) - 1):
                letter_list = list(input_list_idx)
                word = ""            
                letter_list[i], letter_list[i+1] = letter_list[i+1], letter_list[i]
                word = ''.join(letter_list)
                if word in dic_set:
                    return word,"SWAP"
                else:
                    continue 
            else:
                """
                replaces each character in a word with all the letters of the
                alphabet
                checks to see if word is in the dictionary
                """
                letter_list = list(input_list_idx)
                letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'y', 'z' ]                
                for i in range(len(letter_list)):
                    letter_list = list(input_list_idx)
                    word = ""
                    for j in range(len(letters)):
                        letter_list[i] = letters[j]
                        word = ''.join(letter_list)
                        if word in dic_set:
                            return word, "REPLACE"
                        else:
                            continue   
                else:
                    # if no possible combinations make a letter print no match 
                    return input_list_idx, "NO MATCH"

#asks for dictionary file and word file and reads it into a dictionary
dic_file = input("Dictionary file => ").strip()
print(dic_file)
input_file = input("Input file => ").strip()
print(input_file)

dic_set = set()
dic_list = []
for line in open(dic_file):
    dic_list.append(line.strip())
dic_set = set(dic_list)

input_list = []
for line in open(input_file):
    input_list.append(line.strip())

#prints out result of all possible combinations to check if word is in dictionary
for i in range(len(input_list)):
    print("{:15}".format(input_list[i]) +\
          " -> {:15}".format(found_word(dic_set, input_list[i])[0]) +\
          " :" + found_word(dic_set, input_list[i])[1])