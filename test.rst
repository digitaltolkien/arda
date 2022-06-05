>>> from arda.dates import Year, YearDelta, ShireDate

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


>>> print(ShireDate.from_day(1))
2 Yule

>>> ShireDate.from_day(50)
ShireDate(19, 2)

>>> print(ShireDate.from_day(50))
19 Solmath

>>> print(ShireDate.from_day(100))
9 Astron

>>> print(ShireDate.from_day(150))
29 Thrimige

>>> print(ShireDate.from_day(182))
1 Lithe

>>> print(ShireDate.from_day(183))
Mid-year's Day

>>> print(ShireDate.from_day(184))
2 Lithe

>>> print(ShireDate.from_day(200))
16 Afterlithe

>>> print(ShireDate.from_day(250))
6 Halimath

>>> print(ShireDate.from_day(300))
26 Winterfilth

>>> print(ShireDate.from_day(350))
16 Foreyule

>>> print(ShireDate.from_day(365))
1 Yule

>>> print(ShireDate.from_day(1, leap=True))
2 Yule

>>> print(ShireDate.from_day(50, leap=True))
19 Solmath

>>> print(ShireDate.from_day(182, leap=True))
1 Lithe

>>> print(ShireDate.from_day(183, leap=True))
Mid-year's Day

>>> print(ShireDate.from_day(184, leap=True))
Overlithe

>>> print(ShireDate.from_day(185, leap=True))
2 Lithe

>>> ShireDate.from_day(200, leap=True)
ShireDate(15, 7, leap=True)

>>> print(ShireDate.from_day(200, leap=True))
15 Afterlithe

>>> print(ShireDate.from_day(250, leap=True))
5 Halimath

>>> print(ShireDate.from_day(300, leap=True))
25 Winterfilth

>>> print(ShireDate.from_day(350, leap=True))
15 Foreyule

>>> print(ShireDate.from_day(365, leap=True))
30 Foreyule

>>> print(ShireDate.from_day(366, leap=True))
1 Yule

>>> ShireDate.from_day(366, leap=False)
Traceback (most recent call last):
...
ValueError

>>> ShireDate.from_day(-1, leap=True)
Traceback (most recent call last):
...
ValueError

>>> for i in range(1, 366):
...     if ShireDate.from_day(i).to_day() != i:
...         print(i, repr(ShireDate.from_day(i)), ShireDate.from_day(i).to_day())

>>> for i in range(1, 367):
...     if ShireDate.from_day(i, leap=True).to_day(leap=True) != i:
...         print(i, repr(ShireDate.from_day(i, leap=True)), ShireDate.from_day(i, leap=True).to_day(leap=True))
