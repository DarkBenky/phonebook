
class contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def print_contact(self):
        print(self.name, self.number)
class phone_book:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, number):
        self.contacts.append(contact(name, number))
    def remove_contact(self, name, number):
        for i in self.contacts:
            if i.name == name and i.number == number:
                self.contacts.remove(i)
    def rename_contact(self, name, new_name):
        for i in self.contacts:
            if i.name == name:
                i.name = new_name
    def change_number(self, number, new_number):
        for i in self.contacts:
            if i.number == number:
                i.number = new_number
    def search_contact(self, name):
        for i in self.contacts:
            if i.name == name:
                return i.number, i.name
    def split_word(self, word):
        split_word = []
        for i in word:
            split_word.append(i)
        return split_word
    def smart_search(self, name):
        result = []

        split_word = self.split_word(name)
        for i in self.contacts:
            splited_result = self.split_word(i.name)
            for j in split_word:
                if j in splited_result:
                    result.append(i)
        return result
    def print_contact(self):
        for i in self.contacts:
            i.print_contact()
            
    def print_contacts(self,result):
        res = []
        sorted_result = []
        for contact in result:
            if f"{contact.name} {contact.number}" is not res:
                res.append(f"{contact.name} {contact.number}")
        for r in res:
            if r in res:
                sorted_result.append(r)
                res.remove(r)
        print(sorted_result)
phone_book = phone_book()
print("\n")	
phone_book.add_contact("John", "1234567869")
phone_book.add_contact("Mary", "123456789")
phone_book.add_contact("Bobb", "12345567891")
phone_book.add_contact("Marysie", "12345445667891")
phone_book.add_contact("Bob", "1234567891")
phone_book.print_contact()
print("\n")
phone_book.remove_contact("John", "1234567869")
phone_book.print_contact()
print("\n")
phone_book.rename_contact("Mary", "Marys")
phone_book.print_contact()
print("\n")
phone_book.change_number("123456789", "1234567899")
phone_book.print_contact()
print("\n")
phone_book.search_contact("Marys")
print("\n")
r = (phone_book.smart_search("Ma"))
phone_book.print_contacts(r)
