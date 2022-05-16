def twice_as_old(dad_years_old, son_years_old):
    years = 0

    if son_years_old > 0:
        for j in range(1, dad_years_old):
            if (dad_years_old - j == son_years_old * 2) or (dad_years_old + j == son_years_old * 2):
                years = j
    else:
        years = dad_years_old
    return years
