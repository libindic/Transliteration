#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Any Indian Language to any other Indian language transliterator
# Copyright 2008-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email:
# santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in

import os
from cmumapping import *


class CMUDict():
    def __init__(self):
        self.dictionaryfile = os.path.join(os.path.dirname(__file__), \
                'cmudict.0.7a_SPHINX_40')
        self.cmudictionary = None

    def load(self):
        fdict = open(self.dictionaryfile, "r")
        flines = fdict.readlines()
        linecount = len(flines)
        self.cmudictionary = dict()
        for line in flines:
            line = line.strip()
            lhs = line.split()[0]
            rhs = line.split()[1:]
            self.cmudictionary[lhs] = rhs

    def find(self, word):
        if self.cmudictionary == None:
            self.load()
        return self.cmudictionary[word.upper()]

    def pronunciation(self, word, language):
        stripped_word = word.strip('!,.?:')
        punctuations = word[len(stripped_word):]
        try:
            cmu_pronunciation = self.find(stripped_word)
        except KeyError:
            #print "could not find the word" + stripped_word + " in dictionary"
            return word
        pronunciation_str = ""
        if language == "ml_IN":
            for syl in cmu_pronunciation:
                try:
                    pronunciation_str += CMU_MALAYALAM_MAP[syl]
                except KeyError:
                    pronunciation_str += syl
            pronunciation_str = self._fix_vowel_signs_ml(pronunciation_str)

        if language == "kn_IN":
            for symbol in cmu_pronunciation:
                try:
                    pronunciation_str += CMU_KANNADA_MAP[symbol]
                except KeyError:
                    pronunciation_str += symbol
                pronunciation_str = self._fix_vowel_signs_kn(pronunciation_str)
        return (pronunciation_str).decode("utf-8") + punctuations

    def _fix_vowel_signs_ml(self, text):
        text = text.replace("്അ", "")
        text = text.replace("്‍അ", "")
        text = text.replace("്ആ", "ാ")
        text = text.replace("്‍ആ", "ാ")
        text = text.replace("്ഇ", "ി")
        text = text.replace("്‍ഇ", "ി")
        text = text.replace("്ഈ", "ീ")
        text = text.replace("്‍ഈ", "ീ")
        text = text.replace("്ഉ", "ു")
        text = text.replace("്‍ഉ", "ു")
        text = text.replace("്ഊ", "ൂ")
        text = text.replace("്‍ഊ", "ൂ")
        text = text.replace("്റ", "്ര")
        text = text.replace("്എ", "െ")
        text = text.replace("്‍എ", "")
        text = text.replace("്ഏ", "േ")
        text = text.replace("്‍ഏ", "േ")
        text = text.replace("്ഐ", "ൈ")
        text = text.replace("്‍ഐ", "ൈ")
        text = text.replace("്ഒ", "ൊ")
        text = text.replace("്‍ഒ", "ൊ")
        text = text.replace("്ഓ", "ോ")
        text = text.replace("്‍ഓ", "ോ")
        text = text.replace("്ഔ", "ൌ")
        text = text.replace("്‍ഔ", "ൌ")
        text = text.replace("ര്ര", "റ്റ")
        text = text.replace("റ്ര", "റ്റ")
        text = text.replace("ന്‍റ്റ", "ന്റ")
        return text

    def _fix_vowel_signs_kn(self, text):
        text = text.replace("್ಅ", "")
        text = text.replace("್ಆ", "ಾ")
        text = text.replace("್ಇ", "ಿ")
        text = text.replace("್ಈ", "ೀ")
        text = text.replace("್ಉ", "ು")
        text = text.replace("್ಊ", "ೂ")
        text = text.replace("್ಋ", "ೃ")
        text = text.replace("್ಎ", "ೆ")
        text = text.replace("್ಏ", "ೇ")
        text = text.replace("್ಐ", "ೈ")
        text = text.replace("್ಒ", "ೊ")
        text = text.replace("್ಓ", "ೋ")
        text = text.replace("್ಔ", "ೌ")
        return text
