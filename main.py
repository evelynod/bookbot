# Ch 2 L 3 Assignment: 

# 1. Write a new function called get_book_text.
# It takes a filepath as input and returns the contents of the file as a string.

# 2. Write a main function that uses get_book_text with the relative path to your
# frankenstein.txt file to print the entire contents of the book to the console




path_to_file = "books/frankenstein.txt"    


def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()   # f is a file object

    print(file_contents)  
    


def main():
    get_book_text(path_to_file)  
    


    



      
    
main()
