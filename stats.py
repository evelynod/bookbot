

def number_of_words(file_contents) :
    list_of_words = file_contents.split()    #split the file into a list of words
    count = 0                                #iterates for each word in the list
    for word in list_of_words:               #and returns a total count of the words
        count += 1
                                               
    return (count)                             


### The following function came during a conversation with Boots
### and he said it looks good.  

def count_specific_chars(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

    return char_counts

# get_sorted_characters function takes character count dictionary as input
# Returns a list of dictionaries like [{"char" : "r", "num" : 290}, {"char": "a", "num": 25}]
# Sorts from highest count to lowest
# Uses the .sort() method

def get_sorted_characters(char_counts):
    # Convert to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    
    # Sort using .sort() method
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    return char_list