from cryptography.fernet import Fernet
class Password_Manager:
    def __init__(self):
        self.key = None
        self.passwordFile = None
        self.PasswordDict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

#pm = Password_Manager() #(This and create key were used to create the encrypted key needed for the project)
#pm.create_key("mykey.Key")

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def creating_password_file(self, path, intial_values = None):
        self.passwordFile = path

        if intial_values is not None:
            for key, values in intial_values.items():
                self.Add_Password(key, values) #the method

    def loading_password_file(self, path):
        self.passwordFile = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.PasswordDict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()


    def Add_Password(self, site, password):
        self.PasswordDict[site] = password

        if self.passwordFile is not None:
            with open(self.passwordFile, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")
    def Getting_password(self, site):
        return self.PasswordDict[site]


def main(): #menu
    password = {
        "email": "TheAdmin@gmail.com",
        "Instagram" : "Hello_World@123",
        "Else": "0987654321mm"
    }

    #password manager object
    pm = Password_Manager()

    print("""What Would You like to To, Choose your option below? :
    (1) Create a new key
    (2) Load an existing key
    (3) Create a new password file
    (4) Load an existing password file
    (5) Would you like to add a new password
    (6) Get a password
    (q/Q) Quit """)

    done = False
    while not done:
        choice = input("Please make your choice: ")
        if choice == "1":
            path = input("Enter the path: ")
            pm.create_key(path) #the key used for encryption and decryption

        elif    choice == '2':
            path = input("Enter the path: ")
            pm.load_key(path)

        elif    choice == '3':
            path = input("Enter the path: ")
            pm.creating_password_file(path, password)

        elif    choice == '4':
            path = input("Enter the path: ")
            pm.loading_password_file(path)

        elif    choice == '5':
            path = input("Please enter the site: ")
            password = input("Enter the password: ")
            pm.Add_Password(site, password )

        elif    choice == '6':
            site  = input("Which site would you want: ")
            print(f"Password for {site} is {pm.Getting_password(site)}")

        elif    choice == 'q':
            done = True
            print('Goodbye!!!')

        else:
            print("Invalid choice inputted!!!")

if __name__ == "__main__":
    main()

