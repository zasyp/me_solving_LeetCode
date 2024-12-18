def addBinary(a, b):
    num_a = int(a, 2)
    num_b = int(b, 2)

    result = num_a + num_b

    return bin(result)[2:]


print(addBinary("11", "1"))
