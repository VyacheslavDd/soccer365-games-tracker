import os
import constants
import save_parser

class Loader:
    @classmethod
    def load_set(cls):
       if not os.path.exists(constants.SAVE_PATH):
        return Exception("Не существует директории с файлом сохранения.")
       files = os.listdir(constants.SAVE_PATH)
       if not len(files):
           return Exception("Не существует файла сохранения.")
       for file in files:
          if file == constants.SAVE_FILE_TITLE:
             data = save_parser.Parser.parse_save(os.path.join(constants.SAVE_PATH, file))
             return data
       return Exception("Непредвиденная ошибка.")