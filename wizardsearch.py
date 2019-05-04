import textwrap as t

'''
function to read and load \n titles and beasts file
inputs: filename
outputs: a tuple of list of titles, and list of beast sets

'''

def load_file(fname):

    '''
    function to read and load titles and beasts file
    inputs: filename
    outputs: a list of titles, a list of sets of beasts

    reads the lines from the file.
    then split the line into pieces, with "|" as separator
    piece(0) goes to the list => titles
    piece(1..n) goes as a set the list => beasts

    output is a tuple of list of titles, and list of beast sets
    '''

    # initialize separator, list variables
    sep = "|"
    tset = []
    bset = []

    # read one line at a time
    for line in open(fname):

        # strip the line, both sides
        line.strip()
        pieces = line.split(sep)

        # strip individual elements of the pieces list
        pieces = list(x.strip() for x in pieces)
        
        # load pieces(0) to list of titles
        tset.append(pieces[0])

        # create a set of the remaining pieces
        # and append the set to the beasts list
        beast_set = set(pieces[1:])
        bset.append(beast_set)

    return (tset, bset)



'''
function to check if a text is found in any of the list of titles
inputs: text to check, list of titles => test
outputs: the title index, for which the title had a match with the text

'''
def find_title(str_t, tset):
    '''
    function to check if a text is found in any of the list of titles
    inputs: text to check, list of titles => test
    outputs: the title index, for which the title had a match with the text

    '''

    # initialize the title index to be returned to -1
    find_idx = -1

    # loop through the title list, and see if the check-text is found
    # in the ith title. all comparisions done in lower case
    # if found, break and return the index position i
    #
    for i in range(len(tset)):
        if tset[i].casefold().find(str_t.casefold()) > -1:
            find_idx = i
            break

    return(find_idx)


'''
function to collect other titles that have any of the beasts
in a given list of set of beasts 
inputs: the list of titles, the list of set of beasts, the set of beasts to match with <match-set>
outputs: the set of titles that have at least one beast associated with the <match-set>

'''
def find_other_titles(titles, beasts, idxt):
    '''
    function to collect other titles that have any of the beasts
    in a given list of set of beasts 
    inputs: the list of titles, the list of set of beasts, the set of beasts to match with <match-set>
    outputs: the set of titles that have at least one beast associated with the <match-set>

    '''

    # initialize an emtpy set
    ot = set()

    # loop through the list of beast sets
    # intersect our match-set with the ith beast set
    # if we have an intersection, and i <> our current beast set index
    # add the ith title to set ot
    #

    for i in range(len(beasts)):
        isect = beasts[i].intersection(beasts[idxt])
        if isect and i != idxt:
            ot.add(titles[i])

    # delete the temporary intersection set. no longer needed
    #
    del isect

    return ot
    

'''
function to collect unique beasts from a idxt set of beast => {beasts[idxt]}

inputs: the list of set of beasts, the index position of the set of beasts
        from which to get the unique subset
outputs: the subset of unique beasts

'''
def find_unique_beasts(beasts, idxt):
    '''
    function to collect unique beasts from a idxt set of beast => {beasts[idxt]}

    inputs: the list of set of beasts, the index position of the set of beasts
            from which to get the unique subset
    outputs: the subset of unique beasts

    to find unique beasts, we will use the set operation difference_update
    '''

    # copy the set beasts[idxt] to ub. this is our starting set of beasts
    ub = beasts[idxt].copy()

    # loop through the list of set of beasts
    for i in range(len(beasts)):
        # if the target set of beasts is not the same as the source set of beasts
        if i != idxt:
            # update ub to have only those beasts that are found in set beasts[i]
            # by doing this over all values of i, the final unique set saved in ub
            ub.difference_update(beasts[i])

    return ub
    

# read titles and beasts from file titles.txt

pac_fname = "titles.txt"
(titles, beasts) = load_file(pac_fname)

ui = True
while ui:
    utitle = input("Enter a title (stop to end) => ")
    print(utitle)
    print()
    
    if utitle.casefold() == "stop":
        break
    else:
        idxt = find_title(utitle, titles)
        if idxt > -1:

            # wrap print title
            t_lines = "Found the following title: " + titles[idxt]
            t_lines = t.wrap(t_lines)
            for l in t_lines:
                print(l)
           

            # wrap print beasts in title
            bt_lines = "Beasts in this title: " + ', '.join(sorted(beasts[idxt]))
            bt_lines = t.wrap(bt_lines)
            for l in bt_lines:
                print(l)
            print()

            # find and wrap print other titles
            ot = find_other_titles(titles, beasts, idxt)
            ot_lines = "Other titles containing beasts in common: " + ', '.join(sorted(ot))
            ot_lines = t.wrap(ot_lines)
            for l in ot_lines:
                print(l)
            print()

            # find and wrap print unique beasts
            ub = find_unique_beasts(beasts, idxt)
            ub_lines = "Beasts appearing only in this title: " + ', '.join(sorted(ub))
            ub_lines = t.wrap(ub_lines)
            for l in ub_lines:
                print(l)
            print()
            
        else:
            print("This title is not found!")
            print()
   

if __name__ == "__main__":

    pass
