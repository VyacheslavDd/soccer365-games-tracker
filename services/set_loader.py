import os
import common.constants as constants
import services.parsers.save_parser as save_parser

class Loader:
    @classmethod
    def load_set(cls, path):
       data = save_parser.Parser.parse_save(path)
       return data