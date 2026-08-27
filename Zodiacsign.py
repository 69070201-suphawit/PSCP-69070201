"""Zodiacsign"""
zodiac = [
    [1, 19, 'capricorn', 'aquarius'],
    [2, 18, 'aquarius', 'pisces'],
    [3, 20, 'pisces', 'aries'],
    [4, 19, 'aries', 'taurus'],
    [5, 20, 'taurus', 'gemini'],
    [6, 21, 'gemini', 'cancer'],
    [7, 22, 'cancer', 'leo'],
    [8, 22, 'leo', 'virgo'],
    [9, 22, 'virgo', 'libra'],
    [10, 23, 'libra', 'scorpio'],
    [11, 21, 'scorpio', 'sagittarius'],
    [12, 21, 'sagittarius', 'capricorn'],
]
def zodiacsign():
    """Zodiacsign"""
    day = int(input())
    month = int(input())
    for row in zodiac :
        if row[0] == month:
            if day <= row[1]:
                print(row[2])
            else :
                print(row[3])
zodiacsign()
