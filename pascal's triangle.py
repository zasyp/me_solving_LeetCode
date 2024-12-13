def generate(numRows):
    result = []
    if numRows == 0:
        return result
    from math import factorial
    for i in range(numRows):
        row = []
        for j in range(i + 1):
            number = int(factorial(i) / ((factorial(j) * factorial(i - j))))
            row.append(number)
        result.append(row)

    return result

print(generate(5))
