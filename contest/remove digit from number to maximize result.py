class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        max_number = ""

        for i in range(len(number)):
            if number[i] == digit:
                current_number = number[:i] + number[i + 1:]
                if max_number == "" or int(current_number) > int(max_number):
                    max_number = current_number

        return max_number
