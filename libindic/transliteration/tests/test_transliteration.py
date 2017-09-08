#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Transliterator


class TransliterationTest(TestCase):

    def setUp(self):
        super(TransliterationTest, self).setUp()
        self.t = Transliterator()
        self.kn = u"ನಮಸ್ಕಾರ ಇದು ಕನ್ನಡ ಪಠ್ಯ ಟ್ರಾನ್ಸ್ಲಿಟರೇಷನ್ ಪರೀಕ್ಷೆಗಾಗಿ"
        self.hi = u"नमस्कार सिल्पा की दुनिया में आपका स्वागत है"
        self.en = "This is a english text for transliteration"

    def test_KannadaToEnglish(self):
        result = self.t.transliterate(self.kn, "en_US")
        print(result.encode('utf-8'))
        self.assertEqual(result.strip(),
                         "namaskaara idu kannaDa paThya"
                         " TraansliTareshhan parikshhegaagi")

    def test_EnglishToKannada(self):
        result = self.t.transliterate(self.en, "kn_IN")
        print(result.encode('utf-8'))
        self.assertEqual(result.strip(),
                         u"ದಿಸ್ ಇಸ್ ಅ ಇಂಗ್ಗ್ಲಿಷ್ ಟೆಕ್ಸ್ಟ್ ಫೋರ್"
                         " transliteration")

    # def test_KannadaToTamil(self):
        # result = self.t.transliterate(self.kn, "ta_IN")
        # print(result.encode('utf-8'))
        # self.assertEqual(result,
        #                 u"நமஸ்காரஇதுகந்நடபட்யட்ராந்ஸ்லிடரேஷந்பரீக்ஷெகாகி")

    # def test_EnglishToHindi(self):
        # TODO Fix test error
        # result = self.t.transliterate(self.en, "hi_IN")
        # print(result.encode('utf-8'))
        # self.assertEqual(result.strip(),
        #                 u"दिस इज़  इन्गलिष टैकसट फौर transliteration")

    def test_HindiToEnglish(self):
        result = self.t.transliterate(self.hi, "en_US")
        print(result.encode('utf-8'))
        self.assertEqual(result.strip(),
                         u"namaskaar silpaa kee duniyaa mem"
                         " aapakaa svaagath hai")

    def test_HindiToIPA(self):
        result = self.t.transliterate(self.hi, 'IPA')
        print(result.encode('utf-8'))
        self.assertEqual(result.strip(),
                         u"n̪əməskaːɾə silpaː kiː d̪un̪ijaː mɛːm"
                         u" aːpəkaː sʋaːgət̪ə ɦɔ")
