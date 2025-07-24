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

# Current problems:  num_words remains 0.  If I try to only define variables inside functions, 
# they don't remain defined, even if they are "returned".  I don't understand that.

###########################################################################################

# 7/24/25  Realized that .split() results in a list, not an integer.  .split() is just the first 
# step of the number_of_words function.



path_to_file = "books/frankenstein.txt"    
num_words = 0     # Declare variable for the number of words.
file_contents = ""
split_contents = []


def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()   # f is a file object

   # print({file_contents})  
    return file_contents      #file_contents will be used in number_of_words function


def number_of_words(file_contents) :
    
    split_contents = file_contents.split()    #split the file into words. 
 
    return split_contents             
    
    


def main():
    get_book_text(path_to_file)  
    number_of_words(file_contents)  
    print(f"{num_words} words found in the document") 
    print(split_contents)    #testing


    



      
    
main()
