import re

sep_num_regexp = r"(\d{1,3}(?:,\d{3})*\d*)"
float_num_regexp = r"(\d+(\.\d+)?)"


def search_comma_sep_num(text: str):
    """
    Search for a comma separated number in a string.

    :param text: (str) the string to search
    :return: (int) the number
    """
    try:
        sep_num_str = re.search(sep_num_regexp, text).group(1)
        num_str = sep_num_str.replace(",", "")
        num = int(num_str)
        return num
    except Exception:
        raise ValueError(f"Cannot find a comma separated number in the string: {text}")


def search_integer_num(text: str):
    """
    Search for an integer number in a string.

    :param text: (str) the string to search
    :return: (int) the number
    """
    try:
        num_str = re.search(r"(\d+)", text).group(1)
        num = int(num_str)
        return num
    except Exception:
        raise ValueError(f"Cannot find an integer number in the string: {text}")


def search_float_num(text: str):
    """
    Search for a float number in a string.

    :param text: (str) the string to search
    :return: (float) the number
    """
    try:
        float_num_str = re.search(float_num_regexp, text).group(1)
        num_str = float_num_str.replace(",", "")
        num = float(num_str)
        return num
    except Exception:
        raise ValueError(f"Cannot find a float number in the string: {text}")
