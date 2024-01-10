import os
import constants
import save_parser

class Loader:
    _path = os.path.join(".", "saves")

    @classmethod
    def load_set(cls):
       if not os.path.exists(cls._path):
        return [list(), list()]
       files = os.listdir(cls._path)
       if not len(files):
           return [list(), list()]
       for file in files:
          if file == constants.SAVE_FILE_TITLE:
             data = save_parser.Parser.parse_save(os.path.join(cls._path, file))
             return data
       return [list(), list()]