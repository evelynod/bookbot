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
#file_contents = ""
split_contents = []


def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()   # f is a file object

    #print({file_contents})  
    return file_contents      #file_contents will be used in number_of_words function


def number_of_words(file_contents) :
    split_contents = file_contents.split()    #split the file into words. At this point it is 
                                              #listing the words, but not counting them.

    return split_contents     

      
    
    


def main():
    
   # get_book_text(path_to_file)
    my_book_text = get_book_text(path_to_file) #Define new variable for get_book_text return value
    print(f"The first 200 characters: {my_book_text[:200]}")  #test to see if my_book_text works

    ### Now run number_of_words.  The book text was called "file_contents" in the 
    ### get_book_text function, but it is "my_book_text" in this main function.  

    split_text = number_of_words(my_book_text)   #Call number of words function. 
    print(f"Here are the first 200 words in a list: {split_text [:200]}") #This works!!


   
    
    


    



      
    
main()
