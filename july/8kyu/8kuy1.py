def isValid(formula):
    if (formula in formula and 2 in formula) or (formula in formula and 4 in formula):
        return False
    elif formula in formula and 6 not in formula:
        return False
    elif 7 not in formula and 8 not in formula:
        return False
    else:
        return True