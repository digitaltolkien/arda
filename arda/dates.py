class Year:
    FIRST_AGE_LENGTH = 590
    SECOND_AGE_LENGTH = 3441
    THIRD_AGE_LENGTH = 3021
    SR_OFFSET = 1600

    SECOND_AGE_END = FIRST_AGE_LENGTH + SECOND_AGE_LENGTH
    THIRD_AGE_END = SECOND_AGE_END + THIRD_AGE_LENGTH

    def __init__(self, sun_year):
        self.sun_year = sun_year

    @property
    def age(self):
        if self.sun_year <= Year.FIRST_AGE_LENGTH:
            return 1
        elif self.sun_year <= Year.SECOND_AGE_END:
            return 2
        elif self.sun_year <= Year.THIRD_AGE_END:
            return 3
        else:
            return 4

    @property
    def year(self):
        if self.sun_year <= Year.FIRST_AGE_LENGTH:
            return self.sun_year
        elif self.sun_year <= Year.SECOND_AGE_END:
            return self.sun_year - Year.FIRST_AGE_LENGTH
        elif self.sun_year <= Year.THIRD_AGE_END:
            return self.sun_year - Year.SECOND_AGE_END
        else:
            return self.sun_year - Year.THIRD_AGE_END

    @property
    def repr_age(self):
        return {
            1: "FA",
            2: "SA",
            3: "TA",
            4: "FoA",
        }[self.age]

    @property
    def str_age(self):
        return {
            1: "F.A.",
            2: "S.A.",
            3: "T.A.",
            4: "Fo.A.",
        }[self.age]

    @classmethod
    def FA(cls, year):
        return cls(year)

    @classmethod
    def SA(cls, year):
        return cls(year + Year.FIRST_AGE_LENGTH)

    @classmethod
    def TA(cls, year):
        return cls(year + Year.SECOND_AGE_END)

    @classmethod
    def SR(cls, year):
        return cls(year + Year.SECOND_AGE_END + Year.SR_OFFSET)

    @classmethod
    def FoA(cls, year):
        return cls(year + Year.THIRD_AGE_END)

    def __eq__(self, other):
        return isinstance(other, Year) and self.sun_year == other.sun_year

    def __add__(self, other):
        if isinstance(other, YearDelta):
            return self.__class__(self.sun_year + other.years)
        else:
            raise TypeError

    def __sub__(self, other):
        return YearDelta(self.sun_year - other.sun_year)

    def __repr__(self):
        return f"Year.{self.repr_age}({self.year})"

    def __str__(self):
        return f"{self.str_age} {self.year}"


class YearDelta:
    def __init__(self, years):
        self.years = years

    def __eq__(self, other):
        return isinstance(other, YearDelta) and self.years == other.years

    def __repr__(self):
        return f"YearDelta({self.years})"


class ShireDate:
    YULE = 13
    LITHE = 14
    MIDYEAR = 15
    OVERLITHE = 16

    def __init__(self, day, month, leap=False):
        self.day = day
        self.month = month
        self.leap = leap

    @staticmethod
    def month_name(month):
        return [
            None,
            "Afteryule",
            "Solmath",
            "Rethe",
            "Astron",
            "Thrimige",
            "Forelithe",
            "Afterlithe",
            "Wedmath",
            "Halimath",
            "Winterfilth",
            "Blotmath",
            "Foreyule",
            "Yule",
            "Lithe",
            "Mid-year's Day",
            "Overlithe",
        ][month]

    @classmethod
    def from_day(cls, day, leap=False):
        if leap:
            if day == 1:
                return cls(2, ShireDate.YULE, leap)
            elif 1 < day < 182:
                m, d = divmod(day - 2, 30)
                m += 1
                d += 1
                return cls(d, m, leap)
            elif day == 182:
                return cls(1, ShireDate.LITHE, leap)
            elif day == 183:
                return cls(0, ShireDate.MIDYEAR, leap)
            elif day == 184:
                return cls(0, ShireDate.OVERLITHE, leap)
            elif day == 185:
                return cls(2, ShireDate.LITHE, leap)
            elif 185 < day < 366:
                m, d = divmod(day - 186, 30)
                m += 7
                d += 1
                return cls(d, m, leap)
            elif day == 366:
                return cls(1, ShireDate.YULE, leap)
            else:
                raise ValueError
        else:
            if day == 1:
                return cls(2, ShireDate.YULE)
            elif 1 < day < 182:
                m, d = divmod(day - 2, 30)
                m += 1
                d += 1
                return cls(d, m)
            elif day == 182:
                return cls(1, ShireDate.LITHE)
            elif day == 183:
                return cls(0, ShireDate.MIDYEAR)
            elif day == 184:
                return cls(2, ShireDate.LITHE)
            elif 184 < day < 365:
                m, d = divmod(day - 185, 30)
                m += 7
                d += 1
                return cls(d, m)
            elif day == 365:
                return cls(1, ShireDate.YULE)
            else:
                raise ValueError

    def to_day(self, leap=False):
        if self.month == ShireDate.YULE:
            return (366 if leap else 365) if self.day == 1 else 1
        elif self.month == ShireDate.LITHE:
            return 182 if self.day == 1 else (185 if leap else 184)
        elif self.month == ShireDate.MIDYEAR:
            return 183
        elif self.month == ShireDate.OVERLITHE:
            return 184
        elif self.month < 7:
            return 30 * (self.month - 1) + self.day + 1
        else:
            return 30 * (self.month - 1) + self.day + (5 if leap else 4)

    def __repr__(self):
        if self.leap:
            return f"ShireDate({self.day}, {self.month}, leap=True)"
        else:
            return f"ShireDate({self.day}, {self.month})"

    def __str__(self):
        if self.day:
            return f"{self.day} {self.month_name(self.month)}"
        else:
            return f"{self.month_name(self.month)}"
