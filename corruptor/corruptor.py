"""corruptor.py"""
from corruptor.geco import LOOKUP_SURNAME_MISSSPELL, LOOKUP_OCR_VARIATIONS, LOOKUP_PHONETIC_VARIATIONS
from corruptor import factory

class Corruptor():

    def __init__(self):
        self.corruptors = {
            'surname': factory.create_categorical_corruptor(LOOKUP_SURNAME_MISSSPELL),
            'ocr': factory.create_ocr_corruptor(LOOKUP_OCR_VARIATIONS),
            'phonetic': factory.create_phonetic_corruptor(LOOKUP_PHONETIC_VARIATIONS),
            'keyboard': factory.create_keyboard_corruptor(0.5, 0.5),
            'insert': factory.create_edit_corruptor(1.0, 0.0, 0.0, 0.0),
            'delete': factory.create_edit_corruptor(0.0, 1.0, 0.0, 0.0),
            'substitute': factory.create_edit_corruptor(0.0, 0.0, 1.0, 0.0),
            'transpose': factory.create_edit_corruptor(0.0, 0.0, 0.0, 1.0),
        }

    def misspell_surname(self, string):
        return self.corruptors['surname'].corrupt_value(string)

    def ocr_variation(self, string):
        return self.corruptors['ocr'].corrupt_value(string)

    def phonetic_variation(self, string):
        return self.corruptors['phonetic'].corrupt_value(string)

    def typing_error(self, string):
        return self.corruptors['keyboard'].corrupt_value(string)

    def edit_insert(self, string):
        return self.corruptors['insert'].corrupt_value(string)

    def edit_delete(self, string):
        return self.corruptors['delete'].corrupt_value(string)

    def edit_substitute(self, string):
        return self.corruptors['substitute'].corrupt_value(string)

    def edit_transpose(self, string):
        return self.corruptors['transpose'].corrupt_value(string)
