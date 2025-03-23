
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float) 

    # методы для работы с приватными атрибутами
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числом')

    def get_coord(self):
        return self.__x, self.__y





# task

import string
import random 
import re

class EmailValidator:

    def __new__(self):
        return None
    
    def __init__(self, email):
        self.email = email

    @classmethod
    def get_random_email(cls):
        letters = string.ascii_lowercase
        digits = ''.join([str(i) for i in range(10)])
        underscore = '_'
        all_chars = letters + digits + underscore + '.'
        address_part1 = ''.join([random.choice(all_chars) for i in range(random.randint(1, 100))])

        address_part2 = ''.join([random.choice(all_chars) for i in range(random.randint(1, 100))])

        address_part3 = '@gmail.com'

        random_address = address_part1 + address_part2 + address_part3
        return random_address

    """
    - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.
    
    """

    @staticmethod
    def __is_email_str(email) :
        if isinstance(email, str):
            return True
        else:
            return False
    
    @classmethod
    def check_email(cls, email):
        patt =  r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        is_str = EmailValidator.__is_email_str(email)
        if not is_str:
            return False
        if re.match(patt, email) is not None:
            return True 
        else:
            return False
