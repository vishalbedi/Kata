def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman = []
    if num > 1000:
        temp_num = num // 1000
        num -= temp_num * 1000
        while(temp_num > 0):
            roman.append("M")
            temp_num-=1
    if num > 500:
        temp_num = num // 500
        num -= temp_num * 500
        while(temp_num > 0):
            roman.append("D")
            temp_num-=1
    if num > 100:
        temp_num = num // 100
        num -= temp_num * 100
        while(temp_num > 0):
            roman.append("C")
            temp_num-=1
    if num > 50:
        temp_num = num // 50
        num -= temp_num * 50
        while(temp_num > 0):
            roman.append("L")
            temp_num-=1
    if num > 10:
        temp_num = num // 10
        num -= temp_num * 10
        while(temp_num > 0):
            roman.append("X")
            temp_num-=1
    if num > 5:
        temp_num = num // 5
        num -= temp_num * 5
        while(temp_num > 0):
            roman.append("V")
            temp_num-=1
    if num > 0:
        temp_num = num
        num -= temp_num
        while(temp_num > 0):
            roman.append("I")
            temp_num-=1
    return "".join(roman)
