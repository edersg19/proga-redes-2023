﻿# Nombre: Eder Gael Saldaña Galván
# Fecha: 10/Noviembre/2023
# Descripción: 3.4.1.13

class WeekDayError(Exception):
    pass

class Weeker:
    __names = ['Lun','Mar','Mie','Jue','Vie','Sab','Dom']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError
            
    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n ) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n ) % 7

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")