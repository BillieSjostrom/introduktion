"""Parsons programming-problem

Instruktion
===========

All kod som behövs för att lösa uppgiften finns. Raderna behöver byta plats
och indenteras för att få fungerande kod som löser problemet.

Alla docstrings har placerats före kodraderna som ska användas för problemet.

"""


"""Givet två sorterade listor, slå samman dess till en sorterad lista."""
def merge_sorted_lists(l1, l2):
    result = []
    next_value = l1.pop(0)
    if len(l1) == 0:
        while len(l1) > 0 or len(l2) > 0:
            result.append(next_value)
        else:
            return result
            if l1[0] > l2[0]:
                if len(l2) == 0:
                        result.append(next_value)
                        next_value = l2.pop(0)
                        return result
                        if len(l1) > 0 and len(l2) > 0:
                        result.extend(l1)
                        result.extend(l2)
