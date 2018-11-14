#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
import string

single_map  = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""","""'f"*^<''""---~>""")
multi_map   = str.maketrans({
    '€': '<euro>',
    '…': '...',
    '™': '(TM)',
    '‰': '<per mille>',
    '‡': '**',
})
multi_map.update(single_map)


def nfc_equal(str1, str2):
    return unicodedata.normalize('NFC', str1) == unicodedata.normalize('NFC', str2)

def fold_equal(str1, str2):
    return (unicodedata.normalize('NFC', str1).casefold() ==
            unicodedata.normalize('NFC', str2).casefold())

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)


if __name__ == '__main__':
    print('---------------------------------------------------------------------------')

    str1 = 'café'
    str2 = 'cafe\u0301'
    str3 = 'Straße'
    str4 = 'strasse'
    print('café == cafe\\u0301: ' + str((str1 == str2)))
    print('nfc_equal(café, cafe\\u0301): ' + str((nfc_equal(str1, str2))))
    print('nfc_equal(A, a): ' + str((nfc_equal('A', 'a'))))
    print('Straße == strasse: ' + str((str3 == str4)))
    print('nfc_equal(Straße, strasse): ' + str((nfc_equal(str3, str4))))
    print('fold_equal(Straße, strasse): ' + str((fold_equal(str3, str4))))
    print('fold_equal(café, cafe\\u0301): ' + str((fold_equal(str1, str2))))
    print('fold_equal(A, a): ' + str((fold_equal('A', 'a'))))

    print('---------------------------------------------------------------------------')

    str5 = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
    str6 = 'http://en.wikipedia.org/wiki/São_Paulo'
    print('Normal: ' + str5)
    print('Shaved: ' + shave_marks(str5))
    print('Shaved: ' + shave_marks_latin(str5))
    print('Normal: ' + str6)
    print('Shaved: ' + shave_marks(str6))
    print('Shaved: ' + shave_marks_latin(str6))

    print('---------------------------------------------------------------------------')

    print('Normal: ' + str5)
    print('Dewinized: ' + dewinize(str5))
    print('Asciized: ' + asciize(str5))

    print('---------------------------------------------------------------------------')
