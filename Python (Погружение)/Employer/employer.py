class People():
    """
    Класс человек
    """

    def __init__(self, first_name, last_name, patronymic, yaer, gender, city):

        self.first_name = first_name # Имя
        self.last_name = last_name   # Фамилия
        self.patronymic = patronymic # Отчество
        self.__yaer = yaer           # Год рождения
        self.gender = gender         # пол
        self.city = city             # Город проживания

    def birthday(self):
        """
        Метод день рождения
        каждый год возраст увеличивается на 1
        """
        self.__yaer += 1

    def full_name(self):
        """
        Метод получения полного имени
        возвращает ФИО человека
        """
        return self.first_name + '\t' + self.last_name + '\t' + self.patronymic

    def get_year(self):
        """
        Метод возраст
        возвращает возраст человека
        """
        return self.__yaer


class Employer(People):
    """
    Класс работник 
    наследуется от класса человек
    """
    def __init__(self, first_name, last_name, patronymic, yaer, gender, city, ID):
        super().__init__(first_name, last_name, patronymic, yaer, gender, city)
        if len(str(ID)) == 6 and type(ID) == int:
            # Получение ID работника проверка 6 ти значное число и тип данных int
            self.ID = ID

        else:
            self.ID = 100000 # этот ID присваивается если проверка на 6 ти значное число и тип int не пройдена

    def get_level(self):
        """
        Метод получения уровня доступа
        Уровень равен остатку от деления на 7 сумммы цифр в ID
        """
        level = (sum(int(i) for i in str(self.ID))) % 7
        self.level = level
        return self.level

Vasya = Employer('Петя', 'Петров', 'Николаевич', 20, 'Мужской', 'Сочи', 123487) # Пример работы метода получения уровня доступа по ID
Vasya.get_level()
print(Vasya.level)