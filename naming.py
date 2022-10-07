def naming(name: str) -> str:
    res = ''
    for sign in name:
        if sign == '.':
            pass
        elif not (sign.isdigit() or sign.isalpha()):
            res += '_'
        else:
            res += sign
    return res.lower()


if __name__ == '__main__':
    print(naming('4. Median of Two Sorted Arrays'))
