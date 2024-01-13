import os
import constants
import save_parser

class Loader:
    @classmethod
    def load_set(cls, path):
       data = save_parser.Parser.parse_save(path)
       return data