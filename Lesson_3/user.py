class User:
    first_name = 'Имя'
    second_name = 'Фамилия'
 

    def __init__(self, first_name, second_name):
        self.name_first = first_name
        self.name_second = second_name

    def sayFirst_name(self):
        print("Мое имя ", self.name_first)

    def saySecond_name(self):
        print("Мая фамилия: ", self.name_second)

    def sayFull_name(self):
        print('Мои имя и фамилия: ', self.name_first, self.name_second)
