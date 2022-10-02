def naming(name: str) -> str:
    res = ''
    for sign in name:
        if not (sign.isdigit() or sign.isalpha()):
            res += '_'
        else:
            res += sign
    return res.lower()


print(naming('4. Median of Two Sorted Arrays'))
