def twice_as_old(dad_years_old, son_years_old):
    difference = dad_years_old - son_years_old
    twice_as_old = difference * 2
    if dad_years_old >= twice_as_old:
        return dad_years_old - twice_as_old
    else:
        return twice_as_old - dad_years_old
