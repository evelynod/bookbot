

def number_of_words(file_contents) :
    list_of_words = file_contents.split()    #split the file into a list of words
    count = 0                                #iterates for each word in the list
    for word in list_of_words:               #and returns a total count of the words
        count += 1
                                               
    return (count)                             