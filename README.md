Transliteration module provides way to transliterate from 
English to any Indian Language or from any Indian Language
other Indian Language. This module is originally part of
[SILPA](http://silpa.org.in), and currently separated as part
of restructuring.

## Usage ##
`from transliteration import transliterate`
` t = transliterate.Transliterator.get_instance()`
` text = u"ನಮಸ್ಕಾರ"`
` t_text = t.transliterate(text,"ml")`
` print t_text #"നമസ്കാര"`

