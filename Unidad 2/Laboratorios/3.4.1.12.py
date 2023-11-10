# Nombre: Eder Gael Saldaña Galván
# Fecha: 10/Noviembre/2023
# Descripción: 3.4.1.12

class Timer: 
    def __init__(self, hour=0, minute=0, second=0): 
        self.__hour = hour 
        self.__minute = minute 
        self.__second = second 
    def __str__(self):
        __second = self.__second 
        __minute = self.__minute 
        __hour = self.__hour 
        if self.__second < 10: 
            __second = '0' + str(self.__second) 
        if self.__minute < 10: 
            __minute = '0' + str(self.__minute) 
        if self.__hour < 10: 
            __hour = '0' + str(self.__hour) 
        outcome = str(__hour) + ':' + str(__minute) + ':' + str(__second) 
        return outcome 
        
    def next_second(self): 
        self.__second += 1 
        if self.__second == 60: 
            self.__second = 0 
            self.__minute += 1 
            if self.__minute == 60: 
                self.__minute = 0