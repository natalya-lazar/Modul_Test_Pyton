from abc import abstractmethod
import datetime


class Note:

    def __init__(self, id_counter, title: str, msg: str,
                 creation_date=datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"),
                 last_change_date=datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S")):
        self.__id = str(id_counter)
        self.__title = title
        self.__msg = msg
        self.__creation_date = creation_date
        self.last_change_date = last_change_date

    def __str__(self):
        return self.__msg

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def last_change_date(self):
        return self.__last_change_date

    @last_change_date.setter
    def last_change_date(self, value):
        self.__last_change_date = value