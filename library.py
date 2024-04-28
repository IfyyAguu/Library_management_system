import csv
import shutil
import tempfile
import pandas as pd

class Book:
    def __init__(self, title, author, genre, availability_status):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability_status = availability_status

class Library:

    def add_book(self, book):

        #each book should be a dictory 
        a_book = {}
        a_book["Title"] = book.title
        a_book["Author"] = book.author
        a_book["Genre"] = book.genre
        a_book["Availability status"] = book.availability_status 

        

        # add book to the library collection which is .csv file
        with open('library_collection.csv', 'a') as file:
            # Remove leading and trailing spaces from the keys
            heading = [key.strip() for key in a_book.keys()]
            writer = csv.DictWriter(file, delimiter=',', fieldnames=heading)
            #write the column name
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(a_book)
            
            

    def view_collection(self):
        collection = pd.read_csv('library_collection.csv')
        print(collection)




    def borrowing_book(self, book_selection):
        # book_selection = input("Enter name of the book: ")
        #df=pd.read_csv('library_collection.csv')
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

        with open('library_collection.csv', 'r', encoding='utf-8') as file, temp_file:
            readData = csv.DictReader(file)
            writer = csv.DictWriter(temp_file, fieldnames=readData.fieldnames)
            writer.writeheader()
            # Convert reader to list to allow modification
            rows = list(readData)  
            for row in rows:
                if row["Title"]== book_selection:
                    try:
                        if row["Availability status"] == 'Available':
                            print(f"{book_selection} is availble")
                            checkout_book = input("Enter yes or no: ")
                            if checkout_book == 'yes':
                                row["Availability status"] = 'Not available'
                                print(f"{book_selection} has been checked out")
                                row={"Title": row["Title"], "Author": row["Author"], "Genre": row["Genre"], "Availability status": row["Availability status"]}
                                print(row)

                            else:
                                print(f'{book_selection } not checked out')
                            
                        else:
                            raise ValueError(f"{book_selection} is not availble")
                    except ValueError as e:
                        print(e)
                    
                writer.writerow(row)
         
        shutil.move(temp_file.name, 'library_collection.csv')


    
            



    def returning_book(self, book_name):
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

        with open('library_collection.csv', 'r', encoding='utf-8') as file, temp_file:
            readData = csv.DictReader(file)
            writer = csv.DictWriter(temp_file, fieldnames=readData.fieldnames)
            writer.writeheader()
            # Convert reader to list to allow modification
            rows = list(readData)  
            for row in rows:
                if row["Title"]== book_name:
            
                    if row["Availability status"] == 'Not available':
                        row["Availability status"] = 'Available'
                        print(f"{book_name} has been returned")
                        row={"Title": row["Title"], "Author": row["Author"], "Genre": row["Genre"], "Availability status": row["Availability status"]}
                        print(row)

                     
                        
                    
                writer.writerow(row)
         
        shutil.move(temp_file.name, 'library_collection.csv')



# Example:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "Available")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "Available")
book3 = Book("1984", "George Orwell", "Dystopian", "Available")
my_library = Library()
#my_library.add_book(book1)
#my_library.view_collection()
# my_library.borrowing_book("The Great Gatsby")
my_library.returning_book("The Great Gatsby")

