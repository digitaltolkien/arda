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
