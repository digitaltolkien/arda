>>> from arda.pron import display_word, syllabify

>>> for word in [
...     "Isildur",
...     "Aulë",
...     "Eärendil",
...     "Eressëa",
...     "Elrond",
...     "Aragorn",
...     "Tinúviel",
...     "Thingol",
...     "Foalókë",
...     "Ringló",
...     "Angband",
...     "Angmar",
...     "Glorfindel",
...     "Glaurung",
...     "Caradhras",
...     "Orome",
...     "Fëanor",
...     "Ancalima",
...     "Elentári",
...     "Denethor",
...     "Periannath",
...     "Ecthelion",
...     "Pelargir",
...     "silivren",
...     "andúne",
...     "dûn",
... ]:
...     print(word, display_word(syllabify(word)))
Isildur i·SIL·dur
Aulë AU·lë
Eärendil e·ä·REN·dil
Eressëa e·RES·së·a
Elrond EL·rond
Aragorn A·ra·gorn
Tinúviel ti·NÚ·vi·el
Thingol ΘIŊ·gol
Foalókë fo·a·LÓ·kë
Ringló RIŊ·gló
Angband AŊG·band
Angmar AŊG·mar
Glorfindel glor·FIN·del
Glaurung GLAU·ruŋ
Caradhras ca·RAÐ·ras
Orome O·ro·me
Fëanor FË·a·nor
Ancalima an·CA·li·ma
Elentári e·len·TÁ·ri
Denethor DE·ne·θor
Periannath pe·ri·AN·naθ
Ecthelion ec·ΘE·li·on
Pelargir pe·LAR·gir
silivren si·LIV·ren
andúne an·DÚ·ne
dûn DÛN


>>> from arda.pron import to_ipa
>>> to_ipa('c')
'k'

>>> to_ipa('@')
Traceback (most recent call last):
...
ValueError: Can't match: @#

>>> to_ipa('ch')
'χ'

>>> to_ipa('Ioreth')
'jοreθ'

>>> for word in [
...     "Isildur",
...     "Aulë",
...     "Eärendil",
...     "Eressëa",
...     "Elrond",
...     "Aragorn",
...     "Tinúviel",
...     "Thingol",
...     "Foalókë",
...     "Ringló",
...     "Angband",
...     "Angmar",
...     "Glorfindel",
...     "Glaurung",
...     "Caradhras",
...     "Orome",
...     "Fëanor",
...     "Ancalima",
...     "Elentári",
...     "Denethor",
...     "Periannath",
...     "Ecthelion",
...     "Pelargir",
...     "silivren",
...     "andúne",
...     "dûn",
... ]:
...     print(word, to_ipa(word))
Isildur isildur
Aulë ɑule
Eärendil e·ɑrendil
Eressëa eresse·ɑ
Elrond elrond
Aragorn ɑrɑgorn
Tinúviel tinuːviel
Thingol θiŋgol
Foalókë foɑloːke
Ringló riŋgloː
Angband ɑŋgbɑnd
Angmar ɑŋgmɑr
Glorfindel glorfindel
Glaurung glɑuruŋ
Caradhras kɑrɑðrɑs
Orome orome
Fëanor fe·ɑnor
Ancalima ɑnkɑlimɑ
Elentári elentɑːri
Denethor deneθor
Periannath periɑnnɑθ
Ecthelion ekθelion
Pelargir pelɑrgir
silivren silivren
andúne ɑnduːne
dûn duːn

>>> for word in [
...     "Isildur",
...     "Aulë",
...     "Eärendil",
...     "Eressëa",
...     "Elrond",
...     "Aragorn",
...     "Tinúviel",
...     "Thingol",
...     "Foalókë",
...     "Ringló",
...     "Angband",
...     "Angmar",
...     "Glorfindel",
...     "Glaurung",
...     "Caradhras",
...     "Orome",
...     "Fëanor",
...     "Ancalima",
...     "Elentári",
...     "Denethor",
...     "Periannath",
...     "Ecthelion",
...     "Pelargir",
...     "silivren",
...     "andúne",
...     "dûn",
... ]:
...     print(word, display_word(syllabify(to_ipa(word), ipa=True)))
Isildur i·ˈsil·dur
Aulë ˈɑu·le
Eärendil e·ɑ·ˈren·dil
Eressëa e·ˈres·se·ɑ
Elrond ˈel·rond
Aragorn ˈɑ·rɑ·gorn
Tinúviel ti·ˈnuː·vi·el
Thingol ˈθiŋ·gol
Foalókë fo·ɑ·ˈloː·ke
Ringló ˈriŋ·gloː
Angband ˈɑŋg·bɑnd
Angmar ˈɑŋg·mɑr
Glorfindel glor·ˈfin·del
Glaurung ˈglɑu·ruŋ
Caradhras kɑ·ˈrɑð·rɑs
Orome ˈo·ro·me
Fëanor ˈfe·ɑ·nor
Ancalima ɑn·ˈkɑ·li·mɑ
Elentári e·len·ˈtɑː·ri
Denethor ˈde·ne·θor
Periannath pe·ri·ˈɑn·nɑθ
Ecthelion ek·ˈθe·li·on
Pelargir pe·ˈlɑr·gir
silivren si·ˈliv·ren
andúne ɑn·ˈduː·ne
dûn ˈduːn