#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
sys.path.append('..')
import transliteration
import unittest

class TransliterationTest(unittest.TestCase):
    def setUp(self):
        self.t = transliteration.getInstance()
        self.kn = u"ನಮಸ್ಕಾರ ಇದು ಕನ್ನಡ ಪಠ್ಯ ಟ್ರಾನ್ಸ್ಲಿಟರೇಷನ್ ಪರೀಕ್ಷೆಗಾಗಿ"
        self.en = "This is a english text for transliteration"

    def testKannadaToEnglish(self):
        result = self.t.transliterate(self.kn,"en_US")
        print result
        self.assertEqual(result,u"namaskaara idu kannaDa paThya TraansliTareshhan parikshhegaagi")

    def testEnglishToKannada(self):
        result = self.t.transliterate(self.en,"kn_IN")
        print result
        self.assertEqual(result,u"ದಿಸ್ ಇಸ್ ಅ ಇಂಗ್ಗ್ಲಿಷ್ ಟೆಕ್ಸ್ಟ್ ಫೋರ್ transliteration")
        
    def testKannadaToTamil(self):
        result = self.t.transliterate(self.kn,"ml_IN")
        print result
        self.assertEqual(result,u"நமஸ்காரஇதுகந்நடபட்யட்ராந்ஸ்லிடரேஷந்பரீக்ஷெகாகி")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TransliterationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
