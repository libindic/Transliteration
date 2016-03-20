#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../transliteration/')
import core
import unittest

class IPAtransliterationTest(unittest.TestCase):
	def setUp(self):
		self.t = core.getInstance()

		# Dictionary containing words to IPA mapping
		self.D = {'contain':'kənteɪn', 'alphabet':'ælfəbɛt', 'late':'leɪt'}

	def test1(self):
		result = self.t.transliterate_ipa('contain', 'en_US')
		self.assertEqual(result.encode('utf-8'), self.D['contain'])

	def test2(self):
		result = self.t.transliterate_ipa('alphabet', 'en_US')
		self.assertEqual(result.encode('utf-8'), self.D['alphabet'])

	def test3(self):
		result = self.t.transliterate_ipa('late', 'en_US')
		self.assertEqual(result.encode('utf-8'), self.D['late'])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(IPAtransliterationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)