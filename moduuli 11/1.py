class Publication:
    def __init__(self, name):
        self.name = name
#---------------------------------------------------------
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author, self.pages = author, pages
#---------------------------------------------------------
    def print_data(self):
        print(f"Book: {self.name}, Author: {self.author}, Pages: {self.pages}")
#---------------------------------------------------------
class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
#---------------------------------------------------------
    def print_data(self):
        print(f"Magazine: {self.name}, Editor-in-Chief: {self.editor}")
#---------------------------------------------------------
# The program
#---------------------------------------------------------
if __name__ == "__main__":
    for pub in [Magazine("Aku Ankka", "Aki Hyyppä"), Book("Hytti n:o 6", "Rosa Liksom", 200)]:
        pub.print_data()
        print()  

