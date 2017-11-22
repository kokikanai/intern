class a:
    def agdgag(year):
        if year % 4 == 0:
            if year % 100 == 0:
                return True
            elif year % 400 == 0:
                return True
        return False
    print (is_leap_year(2004))
    print (is_leap_year(2100))