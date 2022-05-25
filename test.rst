>>> from arda import Year, YearDelta

>>> isildur_born = Year.SA(3209)
>>> isildur_born
Year.SA(3209)
>>> print(isildur_born)
S.A. 3209

>>> sauron_captured = Year.SA(3262)
>>> isildur_killed = Year.TA(2)

>>> sauron_captured - isildur_born
YearDelta(53)

>>> isildur_killed - isildur_born
YearDelta(234)

>>> elrond_born = Year.FA(532)
>>> elrond_weds = Year.TA(109)

>>> elrond_weds - elrond_born
YearDelta(3608)

>>> arwen_born = Year.TA(241)

>>> arwen_born - elrond_born
YearDelta(3740)

>>> aragorn_born = Year.TA(2931)
>>> aragorn_arwen_wed = Year.TA(3019)

>>> aragorn_arwen_wed - arwen_born
YearDelta(2778)

>>> aragorn_arwen_wed - aragorn_born
YearDelta(88)

>>> aragorn_arwen_wed - elrond_born == YearDelta(6518)
True

>>> Year.TA(3019) == Year.SR(1419)
True

>>> Year.FA(500) + YearDelta(50)
Year.FA(550)

>>> Year.FA(500) + YearDelta(1000)
Year.SA(910)

>>> Year.FA(500) + YearDelta(5000)
Year.TA(1469)

>>> aragorn_dies = Year.FoA(120)

>>> print(aragorn_dies)
Fo.A. 120

>>> aragorn_dies = Year.SR(1541)

>>> aragorn_dies - aragorn_born
YearDelta(210)

>>> aragorn_born + "error"
Traceback (most recent call last):
...
TypeError
