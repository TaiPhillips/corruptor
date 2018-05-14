from corruptor import CorruptDataSet, CorruptCategoricalValue, CorruptValuePhonetic, CorruptValueOCR, CorruptValueKeyboard, CorruptValueEdit
from corruptor import position_mod_normal, position_mod_uniform
from basefunctions import char_set_ascii

surname_misspell_corruptor = CorruptCategoricalValue(
    lookup_file_name = 'lookup-files/surname-misspell.csv',
    has_header_line = False,
    unicode_encoding = 'ascii'
)

ocr_corruptor = CorruptValueOCR(
    position_function = position_mod_normal,
    lookup_file_name = 'lookup-files/ocr-variations.csv',
    has_header_line = False,
    unicode_encoding = 'ascii'
)

keyboard_corruptor = CorruptValueKeyboard(
    position_function = position_mod_normal,
    row_prob = 0.5,
    col_prob = 0.5
)

phonetic_corruptor = CorruptValuePhonetic(
    lookup_file_name = 'lookup-files/phonetic-variations.csv',
    has_header_line = False,
    unicode_encoding = 'ascii'
)

edit_corruptor = CorruptValueEdit(
    position_function = position_mod_normal,
    char_set_funct = char_set_ascii,
    insert_prob = 0.5,
    delete_prob = 0.5,
    substitute_prob = 0.0,
    transpose_prob = 0.0
)

edit_corruptor_numeric = CorruptValueEdit(
    position_function = position_mod_uniform,
    char_set_funct = char_set_ascii,
    insert_prob = 0.25,
    delete_prob = 0.25,
    substitute_prob = 0.25,
    transpose_prob = 0.25
)

n = 2
field_props = {
    'firstname': 0.25,
    'lastname': 0.25,
    'address': 0.25,
    'city': 0.25,
}

field_meths = {
    'firstname': [(0.1, surname_misspell_corruptor), (0.1, ocr_corruptor), (0.1, keyboard_corruptor), (0.7, phonetic_corruptor)],
    'lastname': [(0.1, surname_misspell_corruptor), (0.1, ocr_corruptor), (0.1, keyboard_corruptor), (0.7, phonetic_corruptor)],
    'address': [(0.2, edit_corruptor), (0.4, keyboard_corruptor), (0.4, phonetic_corruptor)],
    'city': [(0.2, edit_corruptor), (0.4, keyboard_corruptor), (0.4, phonetic_corruptor)],
}

data_corruptor = CorruptDataSet(
    number_of_org_records = n,
    number_of_mod_records = 2,
    attribute_name_list = field_props.keys(),
    max_num_dup_per_rec = 2,
    num_dup_dist = 'uniform',
    num_mod_per_rec = 2,
    max_num_mod_per_attr = 1,
    attr_mod_prob_dict = field_props,
    attr_mod_data_dict = field_meths
)

res = data_corruptor.corrupt_records({
    '1-1': ['John', 'Smith', 'Streetware 102', 'London'],
    '2-2': ['Jane', 'Smith', 'Streetware 102', 'London']
})