"""corruptor.py"""
from corruptor.geco import CorruptCategoricalValue, CorruptValuePhonetic, CorruptValueOCR, CorruptValueKeyboard, CorruptValueEdit
from corruptor.geco import LOOKUP_SURNAME_MISSSPELL, LOOKUP_OCR_VARIATIONS, LOOKUP_PHONETIC_VARIATIONS
from corruptor.geco import position_mod_normal, position_mod_uniform, char_set_ascii

class Corruptor():

    def __init__(self):
        self.c_surname = CorruptCategoricalValue(lookup_file_name=LOOKUP_SURNAME_MISSSPELL, has_header_line=False, unicode_encoding='ascii')
        self.c_ocr = CorruptValueOCR(lookup_file_name=LOOKUP_OCR_VARIATIONS, position_function=position_mod_normal, has_header_line=False, unicode_encoding='ascii')
        self.c_phonetic = CorruptValuePhonetic(lookup_file_name=LOOKUP_PHONETIC_VARIATIONS, has_header_line = False, unicode_encoding = 'ascii')
        self.c_keyboard = CorruptValueKeyboard(position_function=position_mod_normal, row_prob=0.5, col_prob=0.5)
        self.c_insert = CorruptValueEdit(position_function=position_mod_normal, char_set_funct=char_set_ascii, insert_prob=1.0, delete_prob=0.0, substitute_prob=0.0, transpose_prob=0.0)
        self.c_delete = CorruptValueEdit(position_function=position_mod_normal, char_set_funct=char_set_ascii, insert_prob=0.0, delete_prob=1.0, substitute_prob=0.0, transpose_prob=0.0)
        self.c_substitute = CorruptValueEdit(position_function=position_mod_normal, char_set_funct=char_set_ascii, insert_prob=0.0, delete_prob=0.0, substitute_prob=1.0, transpose_prob=0.0)
        self.c_transpose = CorruptValueEdit(position_function=position_mod_normal, char_set_funct=char_set_ascii, insert_prob=0.0, delete_prob=0.0, substitute_prob=0.0, transpose_prob=1.0)

    def misspell_surname(self, string):
        return self.c_surname.corrupt_value(string)

    def ocr_variation(self, string):
        return self.c_ocr.corrupt_value(string)

    def phonetic_variation(self, string):
        return self.c_phonetic.corrupt_value(string)

    def typing_error(self, string):
        return self.c_keyboard.corrupt_value(string)

    def edit_insert(self, string):
        return self.c_insert.corrupt_value(string)

    def edit_delete(self, string):
        return self.c_delete.corrupt_value(string)

    def edit_substitute(self, string):
        return self.c_substitute.corrupt_value(string)

    def edit_transpose(self, string):
        return self.c_transpose.corrupt_value(string)
