
class Phone_book:
    def __init__(self):
        self.numbers = []
        self.names = []
    
    def add_number(self, number, name): # add number and name to the phone book
        self.numbers.append(number)
        self.names.append(name)
    
    def remove_contact(self, name , number): # remove
        self.numbers.remove(number)
        self.names.remove(name)
    
    def rename_contact(self, name, new_name):
        count = 0
        for i in self.names:
            count +=1
            if i == name:
                self.names[count-1] = new_name  
    
    def change_number(self, number, new_number):
        count = 0
        for i in self.numbers:
            count +=1
            if i == number:
                self.numbers[count-1] = new_number
            
    def search_contact(self, name):
        count = 0
        for i in self.names:
            count +=1
            if i == name:
                return self.numbers[count-1] , self.names[count-1]
           
    def print_contact(self):
        for i in range(len(self.names)):
            print(self.names[i], self.numbers[i])

phone_book = Phone_book()
phone_book.add_number("1234567869", "John")
phone_book.add_number("123456789", "Mary")
phone_book.add_number("1234567891", "Bob")
phone_book.print_contact()
print ("\n")
phone_book.remove_contact("John", "123456789")
phone_book.print_contact()
print ("\n")
phone_book.rename_contact("Mary", "Marys")
phone_book.print_contact()
phone_book.change_number("123456789", "1234567899")
phone_book.print_contact()
print ("\n")
print(phone_book.search_contact("Marys"))