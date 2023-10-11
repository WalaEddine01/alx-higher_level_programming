#!/usr/bin/python3
'''
This modual contains the MyInt function
'''


class MyInt(int):
    '''
    This is the MyInt class
    '''
    def __init__(self, number):
        self.__number = number

    def __eq__(self, number2):
        return self.__number != number2

    def __ne__(self, number2):
        return self.__number == number2
