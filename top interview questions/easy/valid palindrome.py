def isPalindrome(s: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
    blank = ''
    s = s.lower()
    for symb in s:
        if symb in alphabet:
            blank += symb

    if blank == blank[::-1]:
        return True

    else:
        return False

print(isPalindrome("A man, a plan, a canal: Panama"))