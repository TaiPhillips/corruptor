"""corruptor.py"""
from corruptor.utils import geco_factory as factory

class BasicCorruptor():
    """BasicCorruptor definition"""

    def __init__(self):
        self.corruptions = {
            'none': None,
            'ocr': factory.create_ocr_corruptor(),
            'phonetic': factory.create_phonetic_corruptor(),
            'typo': factory.create_keyboard_corruptor(0.5, 0.5),
            'insert': factory.create_edit_corruptor(1.0, 0.0, 0.0, 0.0),
            'delete': factory.create_edit_corruptor(0.0, 1.0, 0.0, 0.0),
            'replace': factory.create_edit_corruptor(0.0, 0.0, 1.0, 0.0),
            'swap': factory.create_edit_corruptor(0.0, 0.0, 0.0, 1.0),
        }

    def ocr(self, string):
        return self.corruptions['ocr'].corrupt_value(string)

    def phonetic(self, string):
        return self.corruptions['phonetic'].corrupt_value(string)

    def typo(self, string):
        return self.corruptions['typo'].corrupt_value(string)

    def insert(self, string):
        return self.corruptions['insert'].corrupt_value(string)

    def delete(self, string):
        return self.corruptions['delete'].corrupt_value(string)

    def replace(self, string):
        return self.corruptions['replace'].corrupt_value(string)

    def swap(self, string):
        return self.corruptions['swap'].corrupt_value(string)
