class Gregorian:
    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), \
            "Invalid Gregorian Date"
        tmp = 0
        if month<3:
            tmp-=1
        self._julianDay = day-32075 + \
            (1461 *(year + 4800 + tmp) // 4) + \
                (367 * (month - 2 - tmp) // 12) - \
                    (3 * ((year + 4900 + tmp) // 100) // 4)

    def month (self):
        return (self._toGregorian())[0]

    def day(self):
        return (self._toGregorian())[1]
    
    def year(self):
        return (self._toGregorian())[2]
    
    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month += 12
            year -= 1
            return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7
    
    def __str__(self):
        month, day, year = self_toGregorain()
        return "%02d/%02d/%04d" % (month, day, year)

    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay
