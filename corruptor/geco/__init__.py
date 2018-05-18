import os
from corruptor.geco.corruptor import CorruptCategoricalValue, CorruptDataSet, CorruptMissingValue, CorruptValue
from corruptor.geco.corruptor import CorruptValueEdit, CorruptValueKeyboard, CorruptValueOCR, CorruptValuePhonetic
from corruptor.geco.corruptor import position_mod_normal, position_mod_uniform
from corruptor.geco.basefunctions import check_is_not_none, check_is_string, check_is_unicode_string
from corruptor.geco.basefunctions import check_is_string_or_unicode_string, check_is_non_empty_string
from corruptor.geco.basefunctions import check_is_number, check_is_positive, check_is_not_negative
from corruptor.geco.basefunctions import check_is_normalised, check_is_percentage, check_is_integer
from corruptor.geco.basefunctions import check_is_float, check_is_dictionary, check_is_list
from corruptor.geco.basefunctions import check_is_set, check_is_tuple, check_is_flag
from corruptor.geco.basefunctions import check_is_function_or_method, check_unicode_encoding_exists, char_set_ascii
from corruptor.geco.basefunctions import check_is_valid_format_str, float_to_str, str2comma_separated_list
from corruptor.geco.basefunctions import read_csv_file, write_csv_file

LOOKUP_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lookup-files')
LOOKUP_OCR_VARIATIONS = os.path.join(LOOKUP_DIRECTORY, 'ocr-variations.csv')
LOOKUP_PHONETIC_VARIATIONS = os.path.join(LOOKUP_DIRECTORY, 'phonetic-variations.csv')
LOOKUP_SURNAME_MISSSPELL = os.path.join(LOOKUP_DIRECTORY, 'surname-misspell.csv')
