# Ch 2 L 3 Assignment: 

# 1. Write a new function called get_book_text.
# It takes a filepath as input and returns the contents of the file as a string.

# 2. Write a main function that uses get_book_text with the relative path to your
# frankenstein.txt file to print the entire contents of the book to the console

########################################################################################

# Ch 2 L 3 Assignment:

# 1. Write a new function that accepts the text from the book as a string, and returns
#  the number of words in the string. The .split() method will be helpful here
# 2. Instead of printing the books contents, print this message to the console:

# "{num_words} words found in the document"

###########################################################################################




path_to_file = "books/frankenstein.txt"    
num_words = 0     # Declare variable for the number of words.
list_of_words = []


def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()   # f is a file object
      
    return file_contents      #file_contents will be used in number_of_words function



from stats import number_of_words       #Refactoring  The number_of_words function is now in stats.py           
                                               
                                    

def main():
   
   
    my_book_text = get_book_text(path_to_file) 
    word_count = number_of_words(my_book_text,)   #Call number of words function 
    print(f"{word_count} words found in the document")

 
  
 
main()
