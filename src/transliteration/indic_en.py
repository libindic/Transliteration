#!/usr/bin/python
# -*- coding: utf-8 -*-
#indic_en.py
#      
#Copyright 2010 Vasudev Kamath <kamathvasudev@gmail.com>
#      
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU  General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#     
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#      
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#MA 02110-1301, USA.
#
'''
This file contains all language related dictionaries vowel and vowel signs
and function which returns a dictionary or vowel or vowel signs for a language

Trying to make indic_en transliteration more generic
'''

kannada_english_dict = {u'ಅ':'a',u'ಆ':'aa',u'ಇ':'i',u'ಈ':'i',u'ಉ':'u',\
                        u'ಊ':'u',u'ಋ':'rri',u'ಎ':'e',u'ಏ':'e',u'ಐ':'ai',\
                        u'ಒ':'o',u'ಓ':'o',u'ಔ':'au',u'ಂ':'m',u'ಃ':'h',\
                        u'ಕ':'k',u'ಖ':'kh',u'ಗ':'g',u'ಘ':'gh',u'ಙ':'ng',\
                        u'ಚ':'ch',u'ಛ':'chh',u'ಜ':'j',u'ಝ':'jhh',u'ಞ':'nj',\
                        u'ತ':'th',u'ಥ':'thh',u'ದ':'d',u'ಧ':'dh',u'ನ':'n',\
                        u'ಟ':'T',u'ಠ':'Th',u'ಡ':'D',u'ಢ':'Dh',u'ಣ':'N',\
                        u'ಪ':'p',u'ಫ':'ph',u'ಬ':'b',u'ಭ':'bh',u'ಮ':'m',\
                        u'ಯ':'y',u'ರ':'r',u'ಲ':'l',u'ವ':'v',u'ಶ':'sh',\
                        u'ಷ':'shh',u'ಸ':'s',u'ಹ':'h',u'ಳ':'L',\
                        u'ಋ':'rri',u'್':'',u'ಾ':'aa',u'ಿ':'i',u'ೀ':'i',\
                        u'ು':'u',u'ೂ':'u',u'ೃ':'rri',u'ೆ':'e',u'ೇ':'e',\
                        u'ೈ':'ai',u'ೊ':'o',u'ೋ':'o',u'ೌ':'au',\
                        u'ಕ್ಷ':'ksh',u'ತ್ರ':'tr',u'ಜ್ಞ':'jn',\
                        u'೧':'1',u'೨':'2',u'೩':'3',u'೪':'4',u'೫':'5',\
                        u'೬':'6',u'೭':'7',u'೮':'8',u'೯':'9',u'೦':'0'}

kn_vowels = [u'ಅ',u'ಆ',u'ಇ',u'ಈ',u'ಉ',u'ಊ',u'ಋ',u'ಎ',u'ಏ',u'ಐ',\
                 u'ಒ',u'ಓ',u'ಔ']
kn_vowel_signs = [u'್',u'ಾ',u'ಿ',u'ೀ',u'ು',u'ೂ',u'ೃ',u'ೆ',u'ೇ',\
                        u'ೈ',u'ೊ',u'ೋ',u'ೌ',u'ಂ',u'ಃ',u' ']

malayalam_english_dict={u'അ':'a',u'ആ':'aa',u'ഇ':'i',u'ഈ':'ee',u'ഉ':'u',u'ഊ':'oo',u'ഋ':'ri',\
                u'എ':'e',u'ഏ':'e',u'ഐ':'ai',u'ഒ':'o',u'ഓ':'o',u'ഔ':'au',\
                u'ക':'k',u'ഖ':'kh',u'ഗ':'g',u'ഘ':'gh',u'ങ്ങ':'ng',u'ങ':'ng',\
                u'ച':'ch',u'ഛ':'chh',u'ജ':'j',u'ഝ':'jhh',u'ഞ':'nj',\
                u'ട':'t',u'ഠ':'th',u'ഡ':'d',u'ഢ':'dh',u'ണ':'n',\
                u'ത':'th',u'ഥ':'th',u'ദ':'d',u'ധ':'dh',u'ന':'n',\
                u'പ':'p',u'ഫ':'ph',u'ബ':'b',u'ഭ':'bh',u'മ':'m',\
                u'യ':'y',u'ര':'r',u'ല':'l', u'വ':'v', u'റ':'r',\
                u'ശ':'s',u'ഷ':'sh',u'സ':'s', u'ഹ':'h',u'ള':'l',u'ഴ':'zh',\
                u'്':'',u'ം':'m',u'ാ':'aa',u'ി':'i' ,u'ീ':'ee' ,u'ു':'u',\
                u'ൂ':'oo',u'ൃ':'ri' ,u'െ':'e' ,u'േ':'e',\
                u'ൈ':'ai',u'ൊ':'o' ,u'ോ':'oo' ,u'ൗ':'au',  u'ൌ':'ou'}

ml_vowels = [u'അ',u'ആ',u'ഇ',u'ഈ',u'ഉ' ,u'ഊ',u'ഋ', u'എ',u'ഏ',u'ഐ',\
                         u'ഒ',u'ഓ',u'ഔ']                        
ml_vowel_signs = [u'്',u'ം',u'ാ',u'ി',u'ീ',u'ു', u'ൂ',u'ൃ' ,u'െ' ,u'േ',\
                              u'ൈ',u'ൊ' ,u'ോ' ,u'ൗ' , u'ൌ',u'‍']


# P.S: Please declare all language related variables above this and
# fill in the following mapping as you add dictionary vowels and
# vowel_signs for your language


# language dictionary mapping
language_dictionary = {"kn_IN":kannada_english_dict,\
                           "ml_IN":malayalam_english_dict}

# language vowels mapping
language_vowels = {"kn_IN":kn_vowels,"ml_IN":ml_vowels}

# language vowel signs mapping
language_vowel_signs = {"kn_IN":kn_vowel_signs,\
                            "ml_IN":ml_vowel_signs}

# language virama sign mapping
language_virama = {"kn_IN":u"್","ml_IN":u"്"}
# language anuswara sign mapping
language_anuswara = {"kn_IN":u"ಂ","ml_IN":u'ം'}

def get_dictionary_for(lang="ml_IN"):
    """
     Returns the 'language'_english_dict if there
     is no dictionary available for a language then
     return ml_IN dictionary
     i.e cycle through language -> ml_IN -> en_US
    Arguments:
    - `lang`: Language for which dictionary is required
    """
    
    return language_dictionary.get(lang,"ml_IN")

def get_vowels_for(lang="ml_IN"):
    """
    Returns the 'lang'_vowels list. If vowel list
    is not available for a language retrun list for
    ml_IN
    
    Arguments:
    - `lang`: Language for which vowel list should be returned
    """

    return language_vowels.get(lang,"ml_IN")

def get_vowel_signs_for(lang="ml_IN"):
    """
    Returns the 'lang'_vowels list. If vowel list
    is not available for a language retrun list for
    ml_IN
    
    Arguments:
    - `lang`: Language for which vowel signs list should be returned
    """

    return language_vowel_signs.get(lang,"ml_IN")

def get_virama_for(lang="ml_IN"):
    """
    Return the virama symbol for given language
    Arguments:
    - `lang`: Language for which virama symbol should be returned
    """

    return language_virama.get(lang,"ml_IN")

def get_anuswara_for(lang="ml_IN"):
    """
    Return the anuswara symbol for the language
    Arguments:
    - `lang`: Language for which anuswara symbol is needed
    """

    return language_anuswara.get(lang,"ml_IN")
    




    

    

