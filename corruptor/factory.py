"""factory.py"""
from corruptor.geco import CorruptCategoricalValue, CorruptValuePhonetic, CorruptValueOCR, CorruptValueKeyboard, CorruptValueEdit
from corruptor.geco import LOOKUP_SURNAME_MISSSPELL, LOOKUP_OCR_VARIATIONS, LOOKUP_PHONETIC_VARIATIONS
from corruptor.geco import position_mod_normal, char_set_ascii

def create_categorical_corruptor(lookup_file, has_header=False):
    return CorruptCategoricalValue(
        lookup_file_name=lookup_file, 
        has_header_line=has_header,
        unicode_encoding='ascii'
    )

def create_ocr_corruptor(lookup_file, has_header=False):
    return CorruptValueOCR(
        lookup_file_name=lookup_file,
        position_function=position_mod_normal,
        has_header_line=has_header,
        unicode_encoding='ascii'
    )

def create_phonetic_corruptor(lookup_file, has_header=False):
    return CorruptValuePhonetic(
        lookup_file_name=LOOKUP_PHONETIC_VARIATIONS,
        has_header_line=has_header,
        unicode_encoding='ascii'
    )

def create_keyboard_corruptor(row_prob, col_prob):
    return CorruptValueKeyboard(
        position_function=position_mod_normal, 
        row_prob=row_prob, 
        col_prob=col_prob
    )

def create_edit_corruptor(insert_prob, delete_prob, substitute_prob, transpose_prob):
    return CorruptValueEdit(
        position_mod_normal=position_mod_normal,
        char_set_funct=char_set_ascii,
        insert_prob=insert_prob,
        delete_prob=delete_prob,
        substitute_prob=substitute_prob,
        transpose_prob=transpose_prob
    )
