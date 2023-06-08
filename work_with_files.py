class WorkWithFiles:

    def __init__(self, file_name: str):
        self.__file_name = file_name

    def save(self, text):
        with open(self.__file_name, 'w', encoding='utf-8') as data:
            data.write(str(text))

    @property
    def file_name(self):
        return self.__file_name

    def __str__(self):
        with open(self.__file_name, 'r', encoding='utf-8') as data:
            return ''.join(data.readlines())

    def read_lines(self):
        with open(self.__file_name, 'r', encoding='utf-8') as data:
            return data.readlines()