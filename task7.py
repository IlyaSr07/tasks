# сделать функцию которая позволит выводить всю информацию о пользователе полсе того как будет введен корректный пароль
# информация о пользователе ФИО возраст место проживания место работы
# сделать функцию позволяющую создать пользователя

class Userbase():
    def __init__(self):
        self.users = {}
        self.admin = {}
        self.weak = []
        self.medium = []
        self.strong = []

    def checkpassword(self, password):
        symbols = []
        numcheck = 0
        symcheck = 0
        casecheck = 0
        for i in password:
            symbols.append(i)
        for i_2 in symbols:
            if i_2 == '0' or i_2 == '1' or i_2 == '2' or i_2 == '3' or i_2 == '4' or i_2 == '5' or i_2 == '6' or i_2 == '7' or i_2 == '8' or i_2 == '9':
                numcheck = numcheck + 1
            elif i_2 == '!' or i_2 == '@' or i_2 == '#' or i_2 == '$' or i_2 == '%' or i_2 == '^' or i_2 == '&' or i_2 == '*' or i_2 == '(' or i_2 == ')' or i_2 == '-' or i_2 == '_' or i_2 == '+' or i_2 == '=' or i_2 == '`' or i_2 == '~':
                symcheck = symcheck + 1
            elif i_2 == 'Q' or i_2 == 'W' or i_2 == 'E' or i_2 == 'R' or i_2 == 'T' or i_2 == 'Y' or i_2 == 'U' or i_2 == 'I' or i_2 == 'O' or i_2 == 'P' or i_2 == 'A' or i_2 == 'S' or i_2 == 'D' or i_2 == 'F' or i_2 == 'G' or i_2 == 'H' or i_2 == 'J' or i_2 == 'K' or i_2 == 'L' or i_2 == 'Z' or i_2 == 'X' or i_2 == 'C' or i_2 == 'V' or i_2 == 'B' or i_2 == 'N' or i_2 == 'M':
                casecheck = casecheck + 1
        if numcheck < 2 or symcheck < 2 or casecheck < 2 or len(symbols) < 7:
            print('Weak password')
            self.weak.append(password)
        elif len(symbols) > 6 and len(symbols) < 12:
            print('Medium password')
            self.medium.append(password)
        elif len(symbols) >= 12:
            print('Strong password')
            self.strong.append(password)

    def show_all(self):
        print('weak:', self.weak)
        print('medium:', self.medium)
        print('strong:', self.strong)

    def register(self, name, password, age, home, work):
        if name in self.users:
            print('Username already exists')
        else:
            self.users[name] = {'password': password, 'age': age, 'home': home, 'work': work}

    def login(self):
        name = input('name ')
        if name in self.users:
            password = input('password ')
            if self.users[name]['password'] == password:
                print(name, self.users[name])
            else:
                print('Incorrect password')
        else:
            print('Username not found')

    def changeuser(self):
        name = input('name ')
        if name in self.users:
            password = input('password ')
            if self.users[name] == password:
                print(name, self.ages[name], self.homes[name], self.works[name])
            else:
                print('Incorrect password')
        else:
            print('Username not found')

class Admin(Userbase):

    def __init__(self):
        self.p = 0

    def admin_register(self, name, password):
        if name in self.users:
            print('Username already exists')
        else:
            self.users[name] = password
            self.admin[name] = 'yes'

    def admin_login(self):
        name = input('name ')
        if name in self.users:
            if self.admin[name] == 'no':
                print('User is not an administrator')
            else:
                password = input('password ')
                if self.users[name] == password:
                    print('Logged in successfully')
                else:
                    print('Incorrect password')
        else:
            print('Username not found')

    def deleteuser(self, name):
        del self.users[name]
        del self.admin[name]
        print('User deleted sucessfully')

    def edituser(self, name, change, value):
        if change == 'password':
            self.users[name] = value
        if change == 'name':
            self.users
        elif change != 'name' and change != 'ages' and change != 'homes' and change != 'works':
            print('Attribute does not exist')

x = Userbase()
x.register('John', 'qwerty', '23', 'china', 'fishing')
x.login()
