class Book:
    def __init__(self, title, author):
        self.title = title 
#Set the title of the book
        self.author = author 
#Set the author of the book

    def display(self):
        print(self.author + ", written by " + self.title)
#Print the author and title of the book in the format: author, written by title


if __name__ == "__main__":
    book1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")
#Create two book objects with the title and author of the book

    book1.display()
    book2.display()
#Display the author and title of the book

    print("This is assignment 1 part")