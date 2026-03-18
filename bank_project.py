class Bank:
    b_name = "Canara"
    b_loc = "HYD"
    b_ifsc = "CNRB003745"

    def __init__(self,username, upass, uname, uacc, uphn, uemail, acc_type, balance):
        self.username = username
        self.upass = upass
        self.uname = uname
        self.uacc = uacc
        self.uphn = uphn
        self.uemail = uemail
        self.acc_type = acc_type
        self.balance = balance
        self.status = False
        self.check_user()

    def check_user(self):
        b = input("Enter your username: ")
        a = b.lower()
        if(a in self.username):
            self.login()

    def login(self):
        print("----------------------------------------WELCOME TO LOGIN PAGE----------------------------------------")
        acno = int(input("Enter YOUR account number: "))
        if( acno == self.uacc):
            print("Your Account Exists")
            username = input("Enter username: ")
            if(username == self.username):
                c=1
                while c < 4:
                    password = int(input("Enter Password: "))
                    if(password == self.upass):
                        print('Login Successfull!!')
                        self.status = True
                        self.ch_status()
                        break
                    else:
                        print('Invalid Password')
                        print(f"Attempt {c}/3")
                    
                    if(c == 3):
                        print('Access Denied')
                        print("Account Freezed!!!")

                    c+=1
            else:
                print("Invalid Username")
        else:
            print("Account Does not exist")
            
    def display(self):
        print(self.uname, self.uacc, self.uphn, self.uemail, self.acc_type, self.balance)

    def ch_acc(self, new):
        self.acc_type = new

    def update_balance(self):
        new = int(input("enter the amount you want to add in bank: "))
        if(new > 0):
            self.balance = self.balance + new
            print(f"Your amount has been added to account and your current balance is {self.balance}")
        else:
            print("Enter Valid Amount")

    def withdrawl(self):
        amount = int(input("enter the withdrawl amount: "))
        if(self.balance >= amount):
            self.balance = self.balance - amount
            print(f"Withdrawl Successful, Your current balance is {self.balance} ")

    def ch_status(self):
        if(self.status == True):
            print("1 --> Display")
            print("2 --> Check Account type")
            print("3 --> Deposit")
            print("4 --> Withdrawl")
            d = int(input("Enter the mode to work: "))
            if(d == 1):
                self.display()
                
            elif(d == 2):
                 c = input("DO you want to change the account type (Y/N): ").upper()
                 if(c == "Y"):
                    self.ch_acc()
                 else:
                    self.ch_status()
                    
            elif(d == 3):
                c = input("DO you want to deposit the amount in your account (Y/N): ").upper()
                if(c == "Y"):
                    self.update_balance()
                else:
                    self.ch_status()
                    
            elif(d == 4):
                c = input("DO you want to withdraw the amount from your account (Y/N): ").upper()
                if(c == "Y"):
                    self.withdrawl()
                else:
                    self.ch_status()
                    
            else:
                print("Invalid mode" )
                self.ch_status()
                
        else:
            print("Enter Login First")
            self.login()
    
        
u1 = Bank("anurag.123" , 12345678 , "Anurag", 875541235646, 7892345412, "anurag@gmail.com", "savings", 1000)
u2 = Bank("saswat.789" , 78945612 , "Saswat", 654987846541, 2165498765, "saswat@gmail.com", "salaried", 1500)

        

