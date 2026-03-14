import math


def parse_score(value):
    """Attempt to parse a score value into a float in range or return None if invalid."""
    if value is None:
        return None
    v = str(value).strip()
    if v == '' or v.lower() == 'nan':
        return None
    try:
        # accept ints and floats
        if '.' in v:
            n = float(v)
        else:
            n = int(v)
        if math.isnan(n):
            return None
        return float(n)
    except Exception:
        # simple mapping for common word numbers
        words_to_num = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
            'hundred': 100,
        }
        lv = v.lower()
        if lv in words_to_num:
            return float(words_to_num[lv])
        return None
