# программа прнимает от пользователь пароль,
# и проверяет его сложность, пароль должен содержать в себе
# минимум две цифры, два символа и две заглавные буквы
# длина рекомендуемая должна быть не меньше 12 символов
# программа проверяет сложность пароля по градации
# от 1 до 6 символов - слабый
# от 7 до 12 - средний
# от 12 и более  -надежный
# и схорняет введеные пароли
# у программы будет функция show_all,  которая покажет весь список праолей
# отсартированный от самого надежного до самого слабого

class PasswordCheck():
    def __init__(self):
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

x = PasswordCheck()
x.checkpassword('paj')
x.checkpassword('fshdjfsdf')
x.checkpassword('23JG!#fh')
x.checkpassword('23JG!#fhdfjshgj')
x.show_all()
