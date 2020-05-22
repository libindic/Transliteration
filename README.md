Transliteration module provides way to transliterate from
English to any Indian Language or from any Indian Language
other Indian Language. This module is a part of
[libindic](https://libindic.org).

## Setting up ##

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage ##

```bash
source env/bin/activate
python
```

```python
from libindic.transliteration import getInstance
t = getInstance()
text = u"ನಮಸ್ಕಾರ"
t_text = t.transliterate(text, "ml_IN")
print t_text #"നമസ്കാര"
```


for more read the [docs](http://transliteration.rtfd.org)
