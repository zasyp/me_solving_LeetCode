def getSecondLargest(arr: list) -> int:
    unique_values = set(arr)
    if len(unique_values) < 2:
        return -1

    sorted_list = sorted(unique_values, reverse=True)

    return sorted_list[1]