def plusOne(digits):
    str_digits = ''
    for i in range(len(digits)):
        str_digits += str(digits[i])

    big_int = int(str_digits) + 1
    str_digits = str(big_int)
    digits = [int(i) for i in str_digits]
    return digits


print(plusOne([9,9,9]))