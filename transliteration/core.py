#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Any Indian Language to any other Indian language transliterator
# Copyright 2009-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions
# email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in

__all__ = ['Transliterator', 'getInstance']

import string
import normalizer
from cmudict import CMUDict
import indic_en
from langdetect import _detect_lang

lang_bases = { \
        'en_US': 0, 'en_IN': 0, 'hi_IN': 0x0901, 'bn_IN': 0x0981, \
        'pa_IN': 0x0A01, 'gu_IN': 0x0A81, 'or_IN': 0x0B01, 'ta_IN': 0x0B81, \
        'te_IN': 0x0C01, 'kn_IN': 0x0C81, 'ml_IN': 0x0D01 \
        }


class Transliterator:
    def __init__(self):
        self.cmu = CMUDict()
        self.normalizer = normalizer.getInstance()

    def transliterate_en_ml(self, word):
        """
        Transliterate English to Malayalam with the help of
        CMU pronuciation dictionary
        """
        return self.cmu.pronunciation(word, "ml_IN")

    def transliterate_en_kn(self, word):
        """
        Transliterate English to Kannada with the help of
        CMU pronuciation dictionary
        """
        return self.cmu.pronunciation(word, "kn_IN")

    def transliterate_en_xx(self, word, target_lang):
        """
        Transliterate English to any Indian Language.
        """
        if target_lang == "en_IN"  or target_lang == "en_US":
            return word
        if target_lang == "kn_IN":
            tx_str = self.transliterate_en_kn(word)
            return tx_str
        else:
            tx_str = self.transliterate_en_ml(word)

        if target_lang == "ml_IN":
            return tx_str
        #chain it through indic indic transliteratioin
        #first remove malayalam specific zwj
        tx_str = tx_str.replace(u'‍', '')  # remove instances of zwnj
        if tx_str[-1:] == u'്' and (target_lang == "hi_IN" \
                or target_lang == "gu_IN" \
                or target_lang == "bn_IN"):
            tx_str = tx_str[:-(len(u'്'))]  # remove the last virama'
        return self.transliterate_indic_indic(tx_str, "ml_IN", target_lang)

    def transliterate_xx_en(self, word, src_lang):
        """
        Transliterate Indian Language to English.
        """
        if src_lang == "en_IN" or src_lang == "en_US":
            return word

        # TODO: the function is generic now so no need of testing the lanuguage
        # but since the indic_en contains only for kn_IN and ml_IN we need this
        # check.
        # Add all indic language to indic_en
        # remplace this block with single call to indic_en function
        if src_lang == "kn_IN":
            return self.transliterate_indic_en(word, src_lang)
        if not src_lang == "ml_IN":
            word = self.transliterate_indic_indic(word, src_lang, "ml_IN")

        return self.transliterate_indic_en(word, "ml_IN")

    def transliterate_iso15919(self, word, src_language):
        tx_str = ""
        index = 0
        word_length = len(word)
        for chr in word:
            index += 1
            offset = ord(chr) - lang_bases[src_language]
            #76 is the virama offset for all indian languages from its base
            if offset >= 61  and offset <= 76:
                tx_str = tx_str[:-1]  # remove the last 'a'
            if offset > 0 and offset <= 128:
                tx_str = tx_str + charmap["ISO15919"][offset]
            #delete the inherent 'a' at the end of the word from hindi
            if tx_str[-1:] == 'a' and (src_language == "hi_IN"\
                    or src_language == "gu_IN"\
                    or src_language == "bn_IN"):
                if word_length == index and word_length > 1:  # if last letter
                    tx_str = tx_str[:-1]  # remove the last 'a'
        return tx_str .decode("utf-8")

    def transliterate_ipa(self, word, src_language):
        """
        Transliterate the given word in src_language to
        IPA - International Phonetical Alphabet notation.
        """
        tx_str = ""
        index = 0
        word_length = len(word)
        for chr in word:
            index += 1
            if ord(chr) < 255:  # ASCII characters + English
                tx_str += chr
                continue
            offset = ord(chr) - lang_bases[src_language]
            #76 is the virama offset for all indian languages from its base
            if offset >= 61 and offset <= 76:
                tx_str = tx_str[:-(len('ə'))]  # remove the last 'ə'
            if offset > 0 and offset <= 128:
                tx_str = tx_str + charmap["IPA"][offset]
            #delete the inherent 'a' at the end of the word from hindi
            if tx_str[-1:] == 'ə' and (src_language == "hi_IN"\
                    or src_language == "gu_IN"\
                    or src_language == "bn_IN"):
                if word_length == index and word_length > 1:  # if last letter
                    tx_str = tx_str[:-(len('ə'))]  # remove the last 'a'
        return tx_str.decode("utf-8")

    def _malayalam_fixes(self, text):
        try:
            text = text.replace(u"മ് ", u"ം ")
            text = text.replace(u"മ്,", u"ം,")
            text = text.replace(u"മ്.", u"ം.")
            text = text.replace(u"മ്)", u"ം)")
            text = text.replace(u"ഩ", u"ന")
            text = text.replace(u"൤", u".")  # danda by fullstop
        except:
            pass
        return text

    def transliterate_indic_indic(self, word, src_lang, target_lang):
        """
            Transliterate from an Indian languge word
            to another indian language word
        """
        index = 0
        tx_str = ""
        word = self.normalizer.normalize(word)
        if src_lang == "ml_IN" and target_lang != "ml_IN":
            word = word.replace(u"\u200C", u"")
            word = word.replace(u"\u200D", u"")
            #replace all samvruthokaram by u vowels
            word = word.replace(u"ു്", u"")

        for chr in word:
            index += 1
            if chr in string.punctuation or (ord(chr) <= 2304 \
                    and ord(chr) >= 3071):
                tx_str = tx_str + chr
                continue
            offset = ord(chr) + self.getOffset(src_lang, target_lang)
            if(offset > 0):
                tx_str = tx_str + unichr(offset)
            #schwa deletion
            baseoffset = offset - lang_bases[target_lang]
            #76 : virama
            if (index == len(word) and baseoffset == 76 \
                    and (target_lang == "hi_IN" or
                          target_lang == "gu_IN" or
                          target_lang == "pa_IN" or
                          target_lang == "bn_IN")):
                #TODO Add more languages having schwa deletion characteristic
                tx_str = tx_str[:-(len(chr))]  # remove the last 'a'

            if target_lang == "ml_IN" and src_lang == "ta_IN":
                tx_str = tx_str.replace(u"ഩ", u"ന")

            if target_lang == "ta_IN":
                tx_str = tx_str.replace(u'\u0B96', u"க")
                tx_str = tx_str.replace(u'\u0B97', u"க")
                tx_str = tx_str.replace(u'\u0B98', u"க")
                tx_str = tx_str.replace(u'\u0B9B', u"ச")
                tx_str = tx_str.replace(u'\u0B9D', u"ச")
                tx_str = tx_str.replace(u'\u0BA0', u"ட")
                tx_str = tx_str.replace(u'\u0BA1', u"ட")
                tx_str = tx_str.replace(u'\u0BA2', u"ட")
                tx_str = tx_str.replace(u'\u0BA5', u"த")
                tx_str = tx_str.replace(u'\u0BA6', u"த")
                tx_str = tx_str.replace(u'\u0BA7', u"த")
                tx_str = tx_str.replace(u'\u0BAB', u"ப")
                tx_str = tx_str.replace(u'\u0BAC', u"ப")
                tx_str = tx_str.replace(u'\u0BAD', u"ப")
                tx_str = tx_str.replace(u'\u0BC3', u"ிரு")
                tx_str = tx_str.replace(u'ஂ', u'ம்')
        #If target is malayalam, we need to add the virama
        if ((target_lang == "ml_IN") and \
                (src_lang == "hi_IN" or
                src_lang == "gu_IN" or
                src_lang == "pa_IN" or
                src_lang == "bn_IN")
                and tx_str[-1].isalpha()
                ):
            tx_str = tx_str + u"്"
        return tx_str

    def transliterate_indic_en(self, word, src_lang):
        """
        Arguments:
        - `self`:
        - `word`: Word to be transliterated (sentence)
        - `src_lang`: Language from which we need to transilterate
        """

        # Get all the language related stuffs
        dictionary = indic_en.get_dictionary_for(src_lang)
        vowels = indic_en.get_vowels_for(src_lang)
        vowel_signs = indic_en.get_vowel_signs_for(src_lang)
        virama = indic_en.get_virama_for(src_lang)
        anuswara = indic_en.get_anuswara_for(src_lang)

        word_length = len(word)
        index = 0
        tx_string = ""
        while index < word_length:

            # If current charachter is a punctuation symbol
            # skip it.
            # Added to avoid getting extra 'a' to the begining
            # of word next to punctuation symbol
            #

            if word[index] in string.punctuation:
                tx_string += word[index]
                index += 1
                continue

            # Virama = conjucter
            if word[index] == virama:
                index += 1
                continue

            # Get english equivalaent of the charachter.
            try:
                tx_string += dictionary[word[index]]
            except KeyError:
                # If charachter isn't present in the dict
                # just append the charachter to string
                # This case is now handled by punctuation checking
                tx_string += word[index]

            if index + 1 < word_length and not word[index + 1] in vowel_signs \
                    and word[index + 1] in dictionary \
                    and not word[index] in vowels \
                    and not word[index] in vowel_signs:
                tx_string += 'a'

            if index + 1 == word_length and not word[index] in vowel_signs \
                    and word[index] in dictionary:
                tx_string += 'a'

            #handle am sign
            if index + 1 < word_length and word[index + 1] == anuswara \
                    and  not word[index] in vowel_signs:
                tx_string += 'a'
            index += 1
        return tx_string

    def transliterate(self, text, target_lang_code):
        tx_str = ""
        lines = text.split("\n")
        for line in lines:
            words = line.split(" ")
            for word in words:
                if(word.strip() > ""):
                    try:
                        src_lang_code = _detect_lang(word)[word]
                    except:
                        tx_str = tx_str + " " + word
                        continue  # FIXME

                    if target_lang_code == "ISO15919":
                        tx_str = tx_str + self.transliterate_iso15919(word, \
                                src_lang_code) + " "
                        continue

                    if target_lang_code == "IPA":
                        tx_str = tx_str + self.transliterate_ipa(word, \
                                src_lang_code) + " "
                        continue

                    if src_lang_code == "en_US":
                        tx_str = tx_str + self.transliterate_en_xx(word, \
                                target_lang_code) + " "
                        continue

                    if target_lang_code == "en_US" or \
                            target_lang_code == "en_IN":
                        tx_str = tx_str + self.transliterate_xx_en(word, \
                                src_lang_code) + " "
                        continue

                    tx_str += self.transliterate_indic_indic(word, \
                            src_lang_code, target_lang_code)

                    if len(lines) > 1:
                        tx_str += " "

                else:
                    tx_str = tx_str + word
            if len(lines) > 1:
                tx_str += "\n"
        # Language specific fixes
        if target_lang_code == "ml_IN":
            tx_str = self._malayalam_fixes(tx_str)
        return  tx_str

    def getOffset(self, src, target):
        src_id = 0
        target_id = 0
        try:
            src_id = lang_bases[src]
            target_id = lang_bases[target]
            return (target_id - src_id)
        except:
            return 0

    def get_module_name(self):
        return "Transliterator"

    def get_info(self):
        return  "Transliterate the text between any Indian Language"


def getInstance():
    return Transliterator()
