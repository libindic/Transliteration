#!/usr/bin/python
#-*- coding: utf-8 -*-
import unittest
from .. import getInstance
from ..cmudict import remove_halant_at_word_end_hi

class unitsTest(unittest.TestCase):
    def testHalantRemovalWorks(self):
        input = "दिस्"
        expected = "दिस"
        actual = remove_halant_at_word_end_hi(input)
        self.assertEqual(actual, expected)


class TransliterationTest(unittest.TestCase):
    def setUp(self):
        self.t = getInstance()
        self.kn = u"ನಮಸ್ಕಾರ ಇದು ಕನ್ನಡ ಪಠ್ಯ ಟ್ರಾನ್ಸ್ಲಿಟರೇಷನ್ ಪರೀಕ್ಷೆಗಾಗಿ"
        self.hi = u"नमस्कार सिल्पा की दुनिया में आपका स्वागत है"
        self.en = "This is a english text for transliteration"
        self.ml = u"ഇത് ഒരു മലയാളം വാക്യമാണ്"

    def testKannadaToEnglish(self):
        result = self.t.transliterate(self.kn, "en_US")
        self.assertEqual(result.strip(),
                         "namaskaara idu kannaDa paThya"
                         " TraansliTareshhan parikshhegaagi")

    def testEnglishToKannada(self):
        result = self.t.transliterate(self.en, "kn_IN")
        self.assertEqual(result.strip(),
                         "ದಿಸ್ ಇಸ್ ಅ ಇಂಗ್ಗ್ಲಿಷ್ ಟೆಕ್ಸ್ಟ್ ಫೋರ್"
                         " transliteration")

    def testKannadaToTamil(self):
        result = self.t.transliterate(self.kn, "ta_IN")
        expected = u"நமஸ்கார இது கந்நட பட்ய ட்ராந்ஸ்லிடரேஷந் பரீக்ஷெகாகி "
        self.assertEqual(result, expected)
        
        
    def testEnglishToHindi(self):
        result = self.t.transliterate(self.en, "hi_IN")
        self.assertEqual(result.strip(),
                         "दिस इज़ अ इन्ग्लिष टैक्स्ट फौर transliteration")

    def testHindiToEnglish(self):
        result = self.t.transliterate(self.hi, "en_US")
        self.assertEqual(result.strip(),
                         u"namaskaar silpaa kee duniyaa mem"
                         " aapakaa svaagath hai")

    def testHindiToIPA(self):
        result = self.t.transliterate(self.hi, 'IPA')
        self.assertEqual(result.strip(),
                         u"n̪əməskaːɾ silpaː kiː d̪un̪ijaː mɛːm"
                         u" aːpəkaː sʋaːgət̪ ɦɔ")

    def testMalayalamToEnglish(self):
        result = self.t.transliterate(self.ml, "en_US")
        self.assertEqual(result.strip(),
                         "ith oru malayaalam vaakyamaan")

    def testEnglishToMalayalam(self):
        result = self.t.transliterate(self.en, "ml_IN")
        self.assertEqual(result.strip(),
                         "ദിസ് ഇസ് അ ഇങ്ഗ്ലിഷ് റ്റെക്സ്റ്റ് ഫോര്‍"
                         " transliteration")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TransliterationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
