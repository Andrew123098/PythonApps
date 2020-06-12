class Account:                               # Base Class (Shares its methods with Checking)
    """This class defines actions that can 
    be done to a bank account."""            # Docstring
    
    def __init__(self, filepath):            # Constructor (special type of method)
        self.filepath=filepath               # Allows us to use self.filepath anywhere in the class. (called an instance variable)
        with open(filepath, 'r') as file:    
            self.balance=int(file.read())    # Instance Variable
 
    def withdraw(self, amount):              # Method
        self.balance=self.balance - amount   # Instance Variable
        
    def deposit(self, amount):               # Method
        self.balance=self.balance + amount   # Instance Variable
    
    def commit(self):                        # Method
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))    

class Checking(Account):                     # Sub Class (Inheritance: Shares the methods of Account but also has its own methods)
    """This class generates checking account
     objects."""                             # Docstring

    type="checking"                          # Allows us to create variables that are shared by all instances of the class (Class Variable)

    def __init__(self, filepath, fee):       # Constructor
        Account.__init__(self, filepath)     # Define inheritance
        self.fee=fee                         # Instance Variable

    def transfer(self, amount):              # Method
        self.balance=self.balance - amount - self.fee  # Instance variable

jacks_checking=Checking("jack.txt", 1)    # Defines our object (First instantiation of the class)
johns_checking=Checking("john.txt", 1)    # Defines our object (Second instantiation of the class)
account=Account("Balance.txt")            # Defines our object


print(jacks_checking.balance)  # Access the balance attribute
jacks_checking.withdraw(1000)
print(jacks_checking.balance)  # Access the balance attribute
jacks_checking.deposit(500)
print(jacks_checking.balance)  # Access the balance attribute
jacks_checking.transfer(100)
print(jacks_checking.balance)  # Access the balance attribute
jacks_checking.commit()

print(johns_checking.balance)  # Access the balance attribute
johns_checking.withdraw(1000)
print(johns_checking.balance)  # Access the balance attribute
johns_checking.deposit(500)
print(johns_checking.balance)  # Access the balance attribute
johns_checking.transfer(100)
print(johns_checking.balance)  # Access the balance attribute
johns_checking.commit()