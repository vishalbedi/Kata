def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman = []
    if num >= 1000:
        num = add_roman(1000, "M", num, roman)
    if num >= 500:
        if num - 900 >= 0:
            num -= 900
            roman.append("CM")
        else:
            num = add_roman(500, "D", num, roman)
    if num >= 100:
        if num - 400 >= 0:
            num -= 400
            roman.append("CD")
        else:
            num = add_roman(100, "C", num, roman)
    if num >= 50:
        if num - 90 >= 0:
            num -= 90
            roman.append("XC")
        else:
            num = add_roman(50, "L", num, roman)
    if num >= 10:
        if num - 40 >= 0:
            num -= 40
            roman.append("XL")
        else:
            num = add_roman(10, "X", num, roman)
    if num >= 5:
        if num - 9 >= 0:
            num -= 9
            roman.append("IX")
        else:
            num = add_roman(5, "V", num, roman)
    if num >= 1:
        if num - 4>=0:
            num -=4
            roman.append("IV")
        else:
            num = add_roman(1, "I", num, roman)
    return "".join(roman)

def add_roman(int_num, roman_digit, cur_num, roman):
    temp_num = cur_num // int_num
    cur_num -= temp_num * int_num
    while(temp_num > 0):
        roman.append(roman_digit)
        temp_num-=1
    return cur_num
