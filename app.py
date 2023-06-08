from notebook import Notebook
from view import View
from work_with_files import WorkWithFiles


class App:
    def __init__(self):
        self.__filename = 'заметки.csv'
        self.__notebook = Notebook('Тест')
        self.__view = View(self.__notebook)
        self.__work_with_files = WorkWithFiles(self.__filename)

    def start(self):

        try:
            file = open(self.__filename, 'r')
        except IOError:
            file = open(self.__filename, 'w')
            self.__work_with_files.save(';'.join(self.__notebook.fields) + '\n')
        finally:
            file.close()

        actions = {'1': 'список',
                   '2': 'чтение',
                   '3': 'добавить',
                   '4': 'поиск',
                   '5': 'изменить',
                   '6': 'удалить',
                   'q': 'выход'}

        functions = {'1': self.__show_notes,
                     '2': self.__choose_note,
                     '3': self.__add_notes,
                     '4': self.__find_notes,
                     '5': self.__change_notes,
                     '6': self.__delete_notes
                     }

        action = None
        if len(self.__work_with_files.read_lines()) > 1:
            self.__notebook.add_notes_from_csv(str(self.__work_with_files))
        while action != 'q':
            action = self.__view.wait_action(actions, functions)
            if action == 'save':
                self.__work_with_files.save(self.__notebook.csv_format())

    def __show_notes(self):
        self.__view.show_notes(self.__notebook)

    def __add_notes(self):
        title, msg = self.__view.field_input(), self.__view.msg_input()
        confirm = self.__view.confirmation('Подтвердите добавление записи.')
        if confirm:
            self.__notebook.add_note(title, msg)
            return 'save'

    def __find_notes(self):
        field, value = self.__view.find_field(list(self.__notebook.fields.keys()), 'поиска')
        if field != 'q':
            self.__view.show_notes(self.__notebook.find_notes(field, value))

    def __change_notes(self):
        record_id = self.__view.check_id_note('изменить')
        if record_id != 'q':
            field, value = self.__view.find_field(list(self.__notebook.fields.keys())[1:3], 'изменения')
            if field != 'q':
                if self.__view.confirmation('Подтвердите изменение записи'):
                    self.__notebook.change_note(int(record_id), field, value)
                    return 'save'

    def __delete_notes(self):
        record_id = self.__view.check_id_note('удалить')
        if record_id != 'q':
            self.__notebook.delete_note(int(record_id))
            return 'save'

    def __choose_note(self):
        record_id = self.__view.check_id_note('прочитать')
        if record_id != 'q':
            self.__view.show_notes(self.__notebook.find_notes('id', record_id).read_note())