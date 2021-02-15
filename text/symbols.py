""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
# from text import cmudict

_pad        = '_'
# _punctuation = '!\'(),.:;? '
# _special = '-'
# _letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ['@' + s for s in cmudict.valid_symbols]

jyutping = ['<question>', '<space>', '<statement>', '<unk>', 'aa1', 'aa2', 'aa3', 'aa4', 'aa5', 'aa6', 'aai1', 'aai2', 'aai3', 'aai4', 'aai5', 'aai6', 'aak1', 'aak3', 'aak6', 'aam1', 'aam2', 'aam3', 'aam4', 'aam5', 'aam6', 'aan1', 'aan2', 'aan3', 'aan4', 'aan5', 'aan6', 'aang1', 'aang2', 'aang4', 'aang5', 'aang6', 'aap3', 'aap6', 'aat3', 'aat6', 'aau1', 'aau2', 'aau3', 'aau4', 'aau5', 'aau6', 'ai1', 'ai2', 'ai3', 'ai4', 'ai5', 'ai6', 'ak1', 'ak6', 'am1', 'am2', 'am3', 'am4', 'am5', 'am6', 'an1', 'an2', 'an3', 'an4', 'an5', 'an6', 'ang1', 'ang2', 'ang3', 'ang4', 'ang6', 'ap1', 'ap3', 'ap6', 'at1', 'at6', 'au1', 'au2', 'au3', 'au4', 'au5', 'au6', 'b', 'c', 'd', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'ei1', 'ei2', 'ei3', 'ei4', 'ei5', 'ei6', 'ek1', 'ek3', 'ek6', 'eng1', 'eng2', 'eng3', 'eng4', 'eng5', 'eng6', 'eoi1', 'eoi2', 'eoi3', 'eoi4', 'eoi5', 'eoi6', 'eon1', 'eon2', 'eon3', 'eon4', 'eon5', 'eon6', 'eot1', 'eot6', 'ep1', 'f', 'g', 'gw', 'h', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'ik1', 'ik6', 'im1', 'im2', 'im3', 'im4', 'im5', 'im6', 'in1', 'in2', 'in3', 'in4', 'in5', 'in6', 'ing1', 'ing2', 'ing3', 'ing4', 'ing5', 'ing6', 'ip1', 'ip3', 'ip6', 'it1', 'it3', 'it6', 'iu1', 'iu2', 'iu3', 'iu4', 'iu5', 'iu6', 'j', 'k', 'kw', 'l', 'm', 'm4', 'n', 'ng', 'ng2', 'ng4', 'ng5', 'ng6', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'oe1', 'oe3', 'oek3', 'oek6', 'oeng1', 'oeng2', 'oeng3', 'oeng4', 'oeng5', 'oeng6', 'oi1', 'oi2', 'oi3', 'oi4', 'oi6', 'ok1', 'ok3', 'ok6', 'on1', 'on2', 'on3', 'on4', 'on5', 'on6', 'ong1', 'ong2', 'ong3', 'ong4', 'ong5', 'ong6', 'ot3', 'ou1', 'ou2', 'ou3', 'ou4', 'ou5', 'ou6', 'p', 's', 't', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'ui1', 'ui2', 'ui3', 'ui4', 'ui5', 'ui6', 'uk1', 'uk6', 'un1', 'un2', 'un3', 'un4', 'un5', 'un6', 'ung1', 'ung2', 'ung3', 'ung4', 'ung5', 'ung6', 'ut3', 'ut6', 'w', 'yu1', 'yu2', 'yu3', 'yu4', 'yu5', 'yu6', 'yun1', 'yun2', 'yun3', 'yun4', 'yun5', 'yun6', 'yut3', 'yut6', 'z']

# Export all symbols:
# symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet
symbols = [_pad] + jyutping
