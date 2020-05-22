Transliteration module provides way to transliterate from
English to any Indian Language or from any Indian Language
other Indian Language. This module is a part of
[libindic](https://libindic.org).

## Usage ##
    from libindic.transliteration import getInstance
    t = getInstance()
    text = u"ನಮಸ್ಕಾರ"
    t_text = t.transliterate(text, "ml_IN")
    print t_text #"നമസ്കാര"


for more read the [docs](http://transliteration.rtfd.org)
