

def number_of_words(file_contents) :
    list_of_words = file_contents.split()    #split the file into a list of words
    count = 0                                #iterates for each word in the list
    for word in list_of_words:               #and returns a total count of the words
        count += 1
                                               
    return (count)                             


### The following function came during a conversation with Boots
### Use it as a guide for creating mine.  It is in my notebook, with some
### ideas about how I might call it.  MY FUNCTION will need to make everything lowercase, first

def count_specific_chars(text, target_chars):
    text_made_lowercase = text.lower()    
    char_counts = {}
    # Initialize counts for the characters we care about
    for char in target_chars:
        char_counts[char] = 0

    # Iterate through the text ONCE
    for char_in_text in text_made_lowercase:
        # Check if the current character is one we want to count
        if char_in_text in char_counts:
            char_counts[char_in_text] += 1
    return char_counts

